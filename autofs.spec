# TODO:
# - change /net to something FHS-compliant ?
#
# Conditional build:
%bcond_without	ldap	# don't build LDAP extension module
#
Summary:	autofs daemon
Summary(de.UTF-8):	autofs daemon
Summary(es.UTF-8):	Servidor autofs
Summary(fr.UTF-8):	démon autofs
Summary(pl.UTF-8):	Demon autofs
Summary(pt_BR.UTF-8):	Servidor autofs
Summary(tr.UTF-8):	autofs sunucu süreci
Name:		autofs
Version:	5.0.8
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.xz
# Source0-md5:	4ed5271598fb1a76475364a4879c7578
Source1:	%{name}.init
Source2:	%{name}-auto.master
Source3:	%{name}-auto.media
Source4:	%{name}-auto.net
Source5:	%{name}.sysconfig
Patch0:		%{name}-open_max.patch
Patch1:		%{name}-makefile.patch
Patch100:	autofs-5.0.8-fix-undefined-authtype_requires_creds-err-if-ldap-en.patch
Patch101:	autofs-5.0.8-fix-master-map-type-check.patch
Patch102:	autofs-5.0.8-fix-task-manager-not-getting-signaled.patch
Patch103:	autofs-5.0.8-allow-with-systemd-to-take-a-path-arg.patch
Patch104:	autofs-5.0.8-fix-WITH_LIBTIRPC-function-name.patch
Patch105:	autofs-5.0.8-fix-ipv6-libtirpc-getport.patch
Patch106:	autofs-5.0.8-fix-allow-with-systemd-to-take-a-path-arg.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
BuildRequires:	bison
BuildRequires:	e2fsprogs
BuildRequires:	flex
BuildRequires:	heimdal-devel
BuildRequires:	hesiod-devel
BuildRequires:	libtirpc-devel
BuildRequires:	libxml2-devel
BuildRequires:	mount
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	rpmbuild(macros) >= 1.647
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	mktemp
Requires:	rc-scripts
Requires:	systemd-units >= 0.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/autofs
%define		filterout_ld	-Wl,--as-needed

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them. This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de.UTF-8
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert.
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches
einschließen.

%description -l es.UTF-8
Autofs es un servidor que monta automáticamente sistemas de archivos
cuando los usa, y los desmonta, más tarde, al terminar de usarlos.
Incluyendo sistemas de archivo en red, CD-ROMS, disquetes, etc.

%description -l fr.UTF-8
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus.
Cela inclus les systèmes de fichiers réseau, les CD-ROMs, les
disquettes, etc.

%description -l pl.UTF-8
Autofs jest demonem, który montuje automatycznie systemy plików jeżeli
je używasz i odmontowuje później, jeżeli ich nie używasz. Może
montować sieciowy system plików, CD-romy, stacje dyskietek i inne.

%description -l pt_BR.UTF-8
O autofs é um servidor que monta automaticamente sistemas de arquivos
quando estes forem usados, desmontando-os mais tarde quando não
estiverem mais em uso. Incluindo sistemas de arquivo em rede, CD-ROMS,
disquetes, etc.

%description -l tr.UTF-8
autofs, kullanılan dosya sistemlerini gerek olunca kendiliğinden
bağlar ve kullanımları sona erince yine kendiliğinden çözer. Bu işlem,
ağ dosya sistemleri, CD-ROM'lar ve disketler üzerinde yapılabilir.

%package ldap
Summary:	LDAP lookup module for autofs
Summary(pl.UTF-8):	Moduł LDAP dla autofs
Summary(pt_BR.UTF-8):	Suporte a mapas LDAP para o pacote autofs
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap
This package contains the autofs module necessary to use automount
maps stored on an LDAP server.

%description ldap -l pl.UTF-8
Ten pakiet zawiera moduł autofs potrzebny do używania map automounta
trzymanych na serwerze LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1

%build
%{__autoconf}

export initdir=/etc/rc.d/init.d
%configure \
	--with-openldap=%{?with_ldap:yes}%{!?with_ldap:no} \
	--enable-force-shutdown=yes \
	--with-confdir=%{_sysconfdir} \
	--with-mapdir=%{_sysconfdir} \
	--with-libtirpc \
	--with-systemd=%{systemdunitdir}

%{__make} -j1 \
	initdir=/etc/rc.d/init.d \
	CC="%{__cc}" \
	DAEMON_CFLAGS="-fPIE %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/misc,/net,%{_sbindir},%{_libdir}/autofs,%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,autofs,sysconfig}

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/autofs

install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/auto.master
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/auto.media
install %{SOURCE4} 	$RPM_BUILD_ROOT%{_sysconfdir}/auto.net
install %{SOURCE5} 	$RPM_BUILD_ROOT/etc/sysconfig/autofs

touch $RPM_BUILD_ROOT%{_sysconfdir}/auto.{home,var,tmp}

# replaced in PLD by auto.media
rm $RPM_BUILD_ROOT%{_sysconfdir}/auto.misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs
# triggerpostun would get called after %%post
if [ -f /var/lock/subsys/automount ]; then
	mv /var/lock/subsys/{automount,autofs}
fi
%service autofs restart "autofs daemon"
%systemd_post autofs.service

%preun
if [ "$1" = "0" ]; then
	%service autofs stop
	/sbin/chkconfig --del autofs
fi
%systemd_preun autofs.service

%postun
%systemd_reload

%triggerpostun -- autofs < 5.0.8-1
%systemd_trigger autofs.service

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README*
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/autofs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.home
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.master
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.media
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.net
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.smb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.tmp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.var
%attr(754,root,root) /etc/rc.d/init.d/autofs
%{systemdunitdir}/autofs.service
%attr(755,root,root) %{_sbindir}/automount
%dir /net
%dir %{_libdir}/autofs
%attr(755,root,root) %{_libdir}/autofs/lookup_dir.so
%attr(755,root,root) %{_libdir}/autofs/lookup_file.so
%attr(755,root,root) %{_libdir}/autofs/lookup_files.so
%attr(755,root,root) %{_libdir}/autofs/lookup_hesiod.so
%attr(755,root,root) %{_libdir}/autofs/lookup_hosts.so
%attr(755,root,root) %{_libdir}/autofs/lookup_multi.so
%attr(755,root,root) %{_libdir}/autofs/lookup_nis.so
%attr(755,root,root) %{_libdir}/autofs/lookup_nisplus.so
%attr(755,root,root) %{_libdir}/autofs/lookup_program.so
%attr(755,root,root) %{_libdir}/autofs/lookup_userhome.so
%attr(755,root,root) %{_libdir}/autofs/lookup_yp.so
%attr(755,root,root) %{_libdir}/autofs/mount_afs.so
%attr(755,root,root) %{_libdir}/autofs/mount_autofs.so
%attr(755,root,root) %{_libdir}/autofs/mount_bind.so
%attr(755,root,root) %{_libdir}/autofs/mount_changer.so
%attr(755,root,root) %{_libdir}/autofs/mount_ext2.so
%attr(755,root,root) %{_libdir}/autofs/mount_ext3.so
%attr(755,root,root) %{_libdir}/autofs/mount_ext4.so
%attr(755,root,root) %{_libdir}/autofs/mount_generic.so
%attr(755,root,root) %{_libdir}/autofs/mount_nfs.so
%attr(755,root,root) %{_libdir}/autofs/mount_nfs4.so
%attr(755,root,root) %{_libdir}/autofs/parse_hesiod.so
%attr(755,root,root) %{_libdir}/autofs/parse_sun.so
%{_mandir}/man[58]/*

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs_ldap_auth.conf
%attr(755,root,root) %{_libdir}/autofs/lookup_ldap.so
%attr(755,root,root) %{_libdir}/autofs/lookup_ldaps.so
%endif
