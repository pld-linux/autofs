Summary:	autofs daemon
Summary(de):	autofs daemon 
Summary(fr):	d�mon autofs
Summary(pl):	Demon autofs 
Summary(tr):	autofs sunucu s�reci
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
Autofs jest demonem, kt�ry montuje automatycznie systemy plik�w je�eli
je u�ywasz i odmontowuje p�niej, je�eli ich nie u�ywasz. Mo�e montowa�
sieciowy system plik�w, CD-romy, stacje dyskietek i inne.

%description -l de
autofs ist ein D�mon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie sp�ter bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und �hnliches einschlie�en. 

%description -l fr
autofs est un d�mon qui monte automatiquement les syst�mes de fichiers
lorsqu'on les utilise et les d�monte lorsqu'on ne les utilise plus. Cela
inclus les syst�mes de fichiers r�seau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullan�lan dosya sistemlerini gerek olunca kendili�inden ba�lar
ve kullan�mlar� sona erince yine kendili�inden ��zer. Bu i�lem, a� dosya
sistemleri, CD-ROM'lar ve disketler �zerinde yap�labilir.

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
