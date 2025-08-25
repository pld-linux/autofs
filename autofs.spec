# TODO:
# - change /net to something FHS-compliant ?
#
# Conditional build:
%bcond_without	hesiod	# Hesiod support
%bcond_without	ldap	# LDAP extension module
#
Summary:	autofs daemon
Summary(de.UTF-8):	autofs daemon
Summary(es.UTF-8):	Servidor autofs
Summary(fr.UTF-8):	démon autofs
Summary(pl.UTF-8):	Demon autofs
Summary(pt_BR.UTF-8):	Servidor autofs
Summary(tr.UTF-8):	autofs sunucu süreci
Name:		autofs
Version:	5.1.9
Release:	4
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	https://www.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.xz
# Source0-md5:	06fb59a03c82364a0d788435b6853d70
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-systemd-service.patch
Patch1:		cifs-creds-path.patch
Patch2:		fix-nfs4-mounts-in-auto-net.patch
Patch3:		cleanup-master-map.patch
# https://www.kernel.org/pub/linux/daemons/autofs/v5/patches-5.2.0/
Patch100:	autofs-5.1.9-update-configure.patch
Patch101:	autofs-5.1.9-fix-ldap_parse_page_control-check.patch
Patch102:	autofs-5.1.9-fix-crash-in-make_options_string.patch
Patch103:	autofs-5.1.9-Fix-incompatible-function-pointer-types-in-cyrus-sasl-module.patch
Patch104:	autofs-5.1.9-fix-always-recreate-credential-cache.patch
Patch105:	autofs-5.1.9-fix-changelog.patch
Patch106:	autofs-5.1.9-fix-amd-external-mount-error-handling.patch
Patch107:	autofs-5.1.9-fix-amd-external-mount-mount-handling.patch
Patch108:	autofs-5.1.9-dont-free-ext-mount-if-mounted.patch
Patch109:	autofs-5.1.9-refactor-amd-function-do_program_mount.patch
Patch110:	autofs-5.1.9-refactor-amd-function-umount_amd_ext_mount.patch
Patch111:	autofs-5.1.9-add-flags-argument-to-amd-do_program_mount.patch
Patch112:	autofs-5.1.9-fix-amd-cache-options-not-copied.patch
Patch113:	autofs-5.1.9-seperate-amd-mount-and-entry-flags.patch
Patch114:	autofs-5.1.9-make-ioctl-ops-timeout-handle-per-dentry-expire.patch
Patch115:	autofs-5.1.9-refactor-amd-mount-options-handling.patch
Patch116:	autofs-5.1.9-add-some-unimplemented-amd-map-options.patch
Patch117:	autofs-5.1.9-fix-get-parent-multi-mount-check-in-try_remount.patch
Patch118:	autofs-5.1.9-fix-deadlock-in-remount.patch
URL:		https://git.kernel.org/pub/scm/linux/storage/autofs/autofs.git
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cyrus-sasl-devel >= 2
BuildRequires:	e2fsprogs
BuildRequires:	flex
BuildRequires:	heimdal-devel
%{?with_hesiod:BuildRequires:	hesiod-devel}
BuildRequires:	libnsl-devel
BuildRequires:	libtirpc-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	mount
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
przechowywanych na serwerze LDAP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%patch -P100 -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1
%patch -P105 -p1
%patch -P106 -p1
%patch -P107 -p1
%patch -P108 -p1
%patch -P109 -p1
%patch -P110 -p1
%patch -P111 -p1
%patch -P112 -p1
%patch -P113 -p1
%patch -P114 -p1
%patch -P115 -p1
%patch -P116 -p1
%patch -P117 -p1
%patch -P118 -p1

%build
%{__autoconf}

export initdir=/etc/rc.d/init.d
export piddir=/var/run
export fifodir=/var/run
export flagdir=/var/run
export sssldir=%{_libdir}/sssd/modules
export HAVE_SSS_AUTOFS=1
%configure \
	--enable-force-shutdown \
	--with-confdir=%{_sysconfdir} \
	%{!?with_hesiod:--without-hesiod} \
	--with-libtirpc \
	--with-mapdir=%{_sysconfdir} \
	--with-openldap%{!?with_ldap:=no} \
	--with-systemd=%{systemdunitdir}

CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -j1 \
	initdir=/etc/rc.d/init.d \
	CC="%{__cc}" \
	DONTSTRIP=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/misc,/net,%{_sysconfdir}/{creds,auto.master.d},%{_sbindir},%{_libdir}/autofs,%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install install_samples \
	INSTALLROOT=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/autofs

cp -p %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/autofs

touch $RPM_BUILD_ROOT%{_sysconfdir}/auto.{home,var,tmp}

# replaced in PLD by auto.media
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/auto.misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs
# triggerpostun would get called after %%post
if [ -f /var/lock/subsys/automount ]; then
	mv -f /var/lock/subsys/{automount,autofs}
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
%doc CHANGELOG COPYRIGHT CREDITS README*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/autofs
%dir %{_sysconfdir}
%dir %attr(750,root,root) %{_sysconfdir}/creds
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.home
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.master
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.net
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.smb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.tmp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.var
%attr(754,root,root) /etc/rc.d/init.d/autofs
%{systemdunitdir}/autofs.service
%attr(755,root,root) %{_sbindir}/automount
%dir /net
%attr(755,root,root) %{_libdir}/libautofs.so
%dir %{_libdir}/autofs
%attr(755,root,root) %{_libdir}/autofs/lookup_dir.so
%attr(755,root,root) %{_libdir}/autofs/lookup_file.so
%attr(755,root,root) %{_libdir}/autofs/lookup_files.so
%if %{with hesiod}
%attr(755,root,root) %{_libdir}/autofs/lookup_hesiod.so
%endif
%attr(755,root,root) %{_libdir}/autofs/lookup_hosts.so
%attr(755,root,root) %{_libdir}/autofs/lookup_multi.so
%attr(755,root,root) %{_libdir}/autofs/lookup_nis.so
%attr(755,root,root) %{_libdir}/autofs/lookup_nisplus.so
%attr(755,root,root) %{_libdir}/autofs/lookup_program.so
%attr(755,root,root) %{_libdir}/autofs/lookup_sss.so
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
%attr(755,root,root) %{_libdir}/autofs/parse_amd.so
%if %{with hesiod}
%attr(755,root,root) %{_libdir}/autofs/parse_hesiod.so
%endif
%attr(755,root,root) %{_libdir}/autofs/parse_sun.so
%{_mandir}/man5/auto.master.5*
%{_mandir}/man5/autofs.5*
%{_mandir}/man5/autofs.conf.5*
%{_mandir}/man8/autofs.8*
%{_mandir}/man8/automount.8*

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs_ldap_auth.conf
%attr(755,root,root) %{_libdir}/autofs/lookup_ldap.so
%attr(755,root,root) %{_libdir}/autofs/lookup_ldaps.so
%{_mandir}/man5/autofs_ldap_auth.conf.5*
%endif
