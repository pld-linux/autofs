Summary:	autofs daemon
Summary(de):	autofs daemon 
Summary(fr):	démon autofs
Summary(pl):	Demon autofs 
Summary(tr):	autofs sunucu süreci
Name:		autofs
Version:	3.1.3
Release:	3
Copyright:	GPL
Group:		Daemons
Group(pl):	Demony
URL:		ftp://ftp.kernel.org/pub/linux/daemons/autofs
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Patch:		%{name}-%{version}.patch
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/chkconfig
Requires:	mktemp
Exclusivearch:	i386

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
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure \
    --prefix=/usr \
    --sysconfdir=/etc/autofs

make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{sbin,lib/autofs,man/{man5,man8}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,autofs}

make sbindir=$RPM_BUILD_ROOT/usr/sbin \
mandir=$RPM_BUILD_ROOT/usr/man \
autofslibdir=$RPM_BUILD_ROOT/usr/lib/autofs install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/autofs
install samples/auto.* $RPM_BUILD_ROOT/etc/autofs

install -d $RPM_BUILD_ROOT/misc

for i in auto.home auto.misc auto.var auto.tmp; do
touch $RPM_BUILD_ROOT/etc/autofs/$i; done

gzip -9nf $RPM_BUILD_ROOT/usr/man/man[58]/* \
	NEWS README 

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del autofs
fi

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz 

%attr(750,root,root) %config /etc/rc.d/init.d/autofs
%attr(-,root,root,750) %dir /etc/autofs
%attr(640,root,root) %config %verify(not size mtime md5) /etc/autofs/*
%attr(755,root,root) /usr/sbin/automount

%dir /misc

%dir /usr/lib/autofs
%attr(755,root,root) /usr/lib/autofs/*
/usr/man/man[58]/*

%changelog
* Mon Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.1.3-3]
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
