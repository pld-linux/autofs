# TODO:
# What about unpacked files:
#  /etc/auto.master
#  /etc/auto.misc
#  /etc/auto.net
# Probably Source{2,3,5} are obsolete.
Summary:	autofs daemon
Summary(de):	autofs daemon
Summary(es):	Servidor autofs
Summary(fr):	démon autofs
Summary(pl):	Demon autofs
Summary(pt_BR):	Servidor autofs
Summary(tr):	autofs sunucu süreci
Name:		autofs
Version:	4.1.4
Release:	3
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v4/%{name}-%{version}.tar.bz2
# Source0-md5:	7e3949114c00665b4636f0c318179657
Source1:	%{name}.init
Source2:	%{name}-auto.master
Source3:	%{name}-auto.misc
Source4:	%{name}-auto.mnt
Source5:	%{name}-auto.net
Source6:	%{name}.sysconfig
Patch0:		%{name}-open_max.patch
Patch1:		%{name}-hesiod-includes.patch
Patch2:		http://www.kernel.org/pub/linux/daemons/autofs/v4/%{name}-4.1.4-misc-fixes.patch
Patch3:		http://www.kernel.org/pub/linux/daemons/autofs/v4/%{name}-4.1.4-multi-parse-fix.patch
Patch4:		http://www.kernel.org/pub/linux/daemons/autofs/v4/%{name}-4.1.4-no-unlink-upstream.patch
Patch5:		http://www.kernel.org/pub/linux/daemons/autofs/v4/%{name}-4.1.4-non-replicated-ping.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	mktemp
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/autofs

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them. This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert.
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches
einschließen.

%description -l es
Autofs es un servidor que monta automáticamente sistemas de archivos
cuando los usa, y los desmonta, más tarde, al terminar de usarlos.
Incluyendo sistemas de archivo en red, CD-ROMS, disquetes, etc.

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus.
Cela inclus les systèmes de fichiers réseau, les CD-ROMs, les
disquettes, etc.

%description -l pl
Autofs jest demonem, który montuje automatycznie systemy plików je¿eli
je u¿ywasz i odmontowuje pó¼niej, je¿eli ich nie u¿ywasz. Mo¿e
montowaæ sieciowy system plików, CD-romy, stacje dyskietek i inne.

%description -l pt_BR
O autofs é um servidor que monta automaticamente sistemas de arquivos
quando estes forem usados, desmontando-os mais tarde quando não
estiverem mais em uso. Incluindo sistemas de arquivo em rede, CD-ROMS,
disquetes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden
baðlar ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem,
að dosya sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%package ldap
Summary:	LDAP lookup module for autofs
Summary(pl):	Modu³ LDAP dla autofs
Summary(pt_BR):	Suporte a mapas LDAP para o pacote autofs
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap
This package contains the autofs module necessary to use automount
maps stored on an LDAP server.

%description ldap -l pl
Ten pakiet zawiera modu³ autofs potrzebny do u¿ywania map automounta
trzymanych na serwerze LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
chmod a+w configure
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/misc,/net,%{_sbindir},%{_libdir}/autofs,%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,autofs,sysconfig}

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/autofs

install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/auto.master
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/auto.misc
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/auto.mnt
install %{SOURCE5} 	$RPM_BUILD_ROOT%{_sysconfdir}/auto.net
install %{SOURCE6} 	$RPM_BUILD_ROOT/etc/sysconfig/autofs
mv $RPM_BUILD_ROOT/etc/auto.smb $RPM_BUILD_ROOT%{_sysconfdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/auto.{home,misc,var,tmp}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs
# triggerpostun would get called after %%post
if [ -f /var/lock/subsys/automount ]; then
	mv /var/lock/subsys/{automount,autofs}
fi
%service autofs restart "autofs daemon"

%preun
if [ "$1" = "0" ]; then
	%service autofs stop
	/sbin/chkconfig --del autofs
fi

%files
%defattr(644,root,root,755)
%doc README* CHANGELOG

%attr(754,root,root) %config /etc/rc.d/init.d/autofs
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/autofs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.home
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.master
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.misc
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.mnt
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.net
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.smb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.tmp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.var
%attr(755,root,root) %{_sbindir}/automount

%dir /misc
%dir /net

%dir %{_libdir}/autofs
%attr(755,root,root) %{_libdir}/autofs/mount_*
%attr(755,root,root) %{_libdir}/autofs/parse_*
%attr(755,root,root) %{_libdir}/autofs/lookup_[!l]*

%{_mandir}/man[58]/*

%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/autofs/lookup_ldap.so
