Summary:	autofs daemon
Summary(de):	autofs daemon 
Summary(fr):	démon autofs
Summary(pl):	Demon autofs 
Summary(tr):	autofs sunucu süreci
Name:		autofs
Version:	3.1.3
Release:	4
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/%{name}-%{version}.tar.bz2
Source1:	autofs.init
Patch:		autofs.patch
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/chkconfig
Requires:	mktemp

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l pl
Autofs jest demonem, który montuje automatycznie systemy plików je¿eli
je u¿ywasz i odmontowuje pó¼niej, je¿eli ich nie u¿ywasz. Mo¿e montowaæ
sieciowy system plików, CD-romy, stacje dyskietek i inne.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches einschließen. 

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus. Cela
inclus les systèmes de fichiers réseau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden baðlar
ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem, að dosya
sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%prep
%setup -q
%patch -p1 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr \
	--sysconfdir=/etc/autofs
 
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{misc,usr/{sbin,lib/autofs,man/{man5,man8}}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,autofs}

make install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	autofslibdir=$RPM_BUILD_ROOT%{_libdir}/autofs

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/autofs
install samples/auto.* $RPM_BUILD_ROOT/etc/autofs

touch $RPM_BUILD_ROOT/etc/autofs/auto.{home,misc,var,tmp}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/autofs/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[58]/* \
	NEWS README 

%post -n autofs
/sbin/chkconfig --add autofs
if test -r /var/run/autofs.pid; then
	/etc/rc.d/init.d/autofs stop >&2
	/etc/rc.d/init.d/autofs start >&2
else
	echo "Run \"/etc/rc.d/init.d/autofs start\" to start autofs daemon."
fi

%preun -n autofs
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del autofs
	/etc/rc.d/init.d/autofs stop >&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz 

%attr(754,root,root) %config /etc/rc.d/init.d/autofs
%dir /etc/autofs
%attr(644,root,root) %config %verify(not size mtime md5) /etc/autofs/*
%attr(755,root,root) %{_sbindir}/automount

%dir /misc
%dir %{_libdir}/autofs

%attr(755,root,root) %{_libdir}/autofs/*
%{_mandir}/man[58]/*

%changelog
* Tue Apr 20 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.1.3-4]
- recompiled on rpm 3.

* Tue Apr  6 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.1.3-3]
- stripping autofs modules,
- modifications %post, %preun for standarizing this sections; this allow stop
  service on uninstall and automatic restart on upgrade.

* Mon Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
- changed Group(pl) to Demony,
- gzipping documentation,
- added -nf to gzip parameters,
- removed man group from man pages,
- fixed dir permissions,
- cosmetic changes for common l&f.

* Sat Oct 10 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.1.3-1d]
- fixed pl translation,
- fixed invalid modules/Makefile;
- fixed files permissions,
- moved sysconfdir to /etc/autofs,
- fixed rc.autofs to work wiht bash-2.02.1 and higher,
- added some samples auto.* config files.

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.1.1-4d]
- build against glibc-2.1,
- translation modified for pl,
- added %defattr support,
- build from non root's account,
- moved %changelog at the end of spec.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.1.1

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscripts

* Fri Dec 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- Link with -lnsl for glibc compliance.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- exclusivearch for i386 for now, since our kernel packages on
  other platforms don't include autofs yet.
- improvements to initscripts.

* Thu Oct 16 1997 Michael K. Johnson <johnsonm@redhat.com>
- Built package from 0.3.14 for 5.0
