Summary:	autofs daemon
Summary(de):	autofs daemon 
Summary(fr):	d�mon autofs
Summary(pl):	Demon autofs 
Summary(tr):	autofs sunucu s�reci
Name:		autofs
Version:	4.0.0pre6
Release:	1
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/%{name}-%{version}.tar.gz
Source1:	autofs.init
Source2:	autofs-auto.master
Source3:	autofs-auto.misc
Source4:	autofs-auto.mnt
Source5:	autofs-auto.net
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/chkconfig
Requires:	mktemp
Requires:	rc-scripts

%define		_sysconfdir	/etc/autofs

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein D�mon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie sp�ter bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und �hnliches einschlie�en. 

%description -l fr
autofs est un d�mon qui monte automatiquement les syst�mes de fichiers
lorsqu'on les utilise et les d�monte lorsqu'on ne les utilise plus. Cela
inclus les syst�mes de fichiers r�seau, les CD-ROMs, les disquettes, etc.

%description -l pl
Autofs jest demonem, kt�ry montuje automatycznie systemy plik�w je�eli
je u�ywasz i odmontowuje p�niej, je�eli ich nie u�ywasz. Mo�e montowa�
sieciowy system plik�w, CD-romy, stacje dyskietek i inne.

%description -l tr
autofs, kullan�lan dosya sistemlerini gerek olunca kendili�inden ba�lar
ve kullan�mlar� sona erince yine kendili�inden ��zer. Bu i�lem, a� dosya
sistemleri, CD-ROM'lar ve disketler �zerinde yap�labilir.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
 
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{misc,net,%{_sbindir},%{_libdir}/autofs,%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,autofs}

make install \
	INSTALLROOT=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/autofs

install %{SOURCE2}	$RPM_BUILD_ROOT/etc/autofs/auto.master
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/autofs/auto.misc
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/autofs/auto.mnt
install %{SOURCE5} 	$RPM_BUILD_ROOT/etc/autofs/auto.net

touch			$RPM_BUILD_ROOT/etc/autofs/auto.{home,misc,var,tmp}

strip --strip-unneeded	$RPM_BUILD_ROOT%{_libdir}/autofs/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[58]/* \
	NEWS README 

%post
/sbin/chkconfig --add autofs
if test -r /var/lock/subsys/automount; then
	/etc/rc.d/init.d/autofs restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/autofs start\" to start autofs daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del autofs
	if [ -f /var/lock/subsys/automount ]; then
		/etc/rc.d/init.d/autofs stop 1>&2
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz 

%attr(754,root,root) %config /etc/rc.d/init.d/autofs
%dir %{_sysconfdir}
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.home
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.master
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.misc
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.mnt
%attr(755,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.net
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.tmp
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/auto.var
%attr(755,root,root) %{_sbindir}/automount

%dir /misc
%dir /net

%dir %{_libdir}/autofs
%attr(755,root,root) %{_libdir}/autofs/*

%{_mandir}/man[58]/*
