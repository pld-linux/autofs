# TODO:
# - change /net to something FHS-compliant ?
#
Summary:	autofs daemon
Summary(de.UTF-8):	autofs daemon
Summary(es.UTF-8):	Servidor autofs
Summary(fr.UTF-8):	démon autofs
Summary(pl.UTF-8):	Demon autofs
Summary(pt_BR.UTF-8):	Servidor autofs
Summary(tr.UTF-8):	autofs sunucu süreci
Name:		autofs
Version:	5.0.4
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.bz2
# Source0-md5:	2646dde61edd08dd952255558c733c08
Source1:	%{name}.init
Source2:	%{name}-auto.master
Source3:	%{name}-auto.media
Source4:	%{name}-auto.net
Source5:	%{name}.sysconfig
Patch0:		%{name}-open_max.patch
Patch1:		%{name}-5.0.4-fix-dumb-libxml2-check.patch
Patch2:		%{name}-5.0.4-expire-specific-submount-only.patch
Patch3:		%{name}-5.0.4-fix-negative-cache-non-existent-key.patch
Patch4:		%{name}-5.0.4-fix-ldap-detection.patch
Patch5:		%{name}-5.0.4-use-CLOEXEC-flag.patch
Patch6:		%{name}-5.0.4-fix-select-fd-limit.patch
Patch7:		%{name}-5.0.4-make-hash-table-scale-to-thousands-of-entries.patch
Patch8:		%{name}-5.0.4-fix-quoted-mess.patch
Patch9:		%{name}-5.0.4-use-CLOEXEC-flag-setmntent.patch
Patch10:	%{name}-5.0.4-fix-hosts-map-use-after-free.patch
Patch11:	%{name}-5.0.4-uris-list-locking-fix.patch
Patch12:	%{name}-5.0.4-renew-sasl-creds-upon-reconnect-fail.patch
Patch13:	%{name}-5.0.4-library-reload-fix-update.patch
Patch14:	%{name}-5.0.4-force-unlink-umount.patch
Patch15:	%{name}-5.0.4-always-read-file-maps.patch
Patch16:	%{name}-5.0.4-code-analysis-corrections.patch
Patch17:	%{name}-5.0.4-make-MAX_ERR_BUF-and-PARSE_MAX_BUF-use-easier-to-audit.patch
Patch18:	%{name}-5.0.4-easy-alloca-replacements.patch
Patch19:	%{name}-5.0.4-configure-libtirpc.patch
Patch20:	%{name}-5.0.4-ipv6-name-and-address-support.patch
Patch21:	%{name}-5.0.4-ipv6-parse.patch
Patch22:	%{name}-5.0.4-add-missing-changelog-entries.patch
Patch23:	%{name}-5.0.4-use-CLOEXEC-flag-setmntent-include-fix.patch
Patch24:	%{name}-5.0.4-easy-alloca-replacements-fix.patch
Patch25:	%{name}-5.0.4-libxml2-workaround-fix.patch
Patch26:	%{name}-5.0.4-configure-libtirpc-fix.patch
Patch27:	%{name}-5.0.4-add-nfs-mount-proto-default-conf-option.patch
Patch28:	%{name}-5.0.4-fix-bad-token-declare.patch
Patch29:	%{name}-5.0.4-fix-return-start-status-on-fail.patch
Patch30:	%{name}-5.0.4-fix-double-free-in-expire_proc.patch
Patch31:	%{name}-5.0.4-another-easy-alloca-replacements-fix.patch
Patch32:	%{name}-5.0.4-add-lsb-init-script-parameter-block.patch
Patch33:	%{name}-5.0.4-always-read-file-maps-fix.patch
Patch34:	%{name}-5.0.4-use-misc-device.patch
Patch35:	%{name}-5.0.4-fix-restorecon.patch
Patch36:	%{name}-5.0.4-clear-rpc-client-on-lookup-fail.patch
Patch37:	%{name}-5.0.4-fix-lsb-init-script-header.patch
Patch38:	%{name}-5.0.4-fix-memory-leak-reading-ldap-master.patch
Patch39:	%{name}-5.0.4-fix-st_remove_tasks-locking.patch
Patch40:	%{name}-5.0.4-reset-flex-scanner-when-setting-buffer.patch
Patch41:	%{name}-5.0.4-zero-s_magic-is-valid.patch
Patch42:	%{name}-5.0.4-use-percent-hack-for-master.patch
Patch43:	%{name}-5.0.4-use-intr-as-hosts-mount-default.patch
Patch44:	%{name}-5.0.4-fix-kernel-includes.patch
Patch45:	%{name}-5.0.4-dont-umount-existing-direct-mount-on-reread.patch
Patch46:	%{name}-5.0.4-library-reload-fix-update-fix.patch
Patch47:	%{name}-5.0.4-improve-manual-umount-recovery.patch
Patch48:	%{name}-5.0.4-dont-fail-on-ipv6-address-adding-host.patch
Patch49:	%{name}-5.0.4-always-read-file-maps-multi-map-fix.patch
Patch50:	%{name}-5.0.4-always-read-file-maps-key-lookup-fixes.patch
Patch51:	%{name}-5.0.4-use-srv-query-for-domain-dn.patch
Patch52:	%{name}-5.0.4-fix-incorrect-dclist-free.patch
Patch53:	%{name}-5.0.4-srv-lookup-handle-endian.patch
Patch54:	%{name}-5.0.4-library-reload-fix-update-fix-2.patch
Patch55:	%{name}-5.0.4-fix-notify-mount-message-path.patch
Patch56:	%{name}-5.0.4-remount-we-created-mount-point-fix.patch
Patch57:	%{name}-5.0.4-fix-double-free-in-do_sasl_bind.patch
Patch58:	%{name}-5.0.4-manual-umount-recovery-fixes.patch
Patch59:	%{name}-5.0.4-fix-map-type-info-parse-error.patch
Patch60:	%{name}-5.0.4-fix-map-type-info-parse-error-update.patch
Patch61:	%{name}-5.0.4-fix-rpc-fd-leak.patch
Patch62:	%{name}-5.0.4-allow-automount-daemon-to-dump-core.patch
Patch63:	%{name}-5.0.4-fix-pthread-push-order-in-expire_proc_direct.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
BuildRequires:	bison
BuildRequires:	e2fsprogs
BuildRequires:	flex
BuildRequires:	heimdal-devel
BuildRequires:	hesiod-devel
BuildRequires:	libxml2-devel
BuildRequires:	mount
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	mktemp
Requires:	rc-scripts
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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1

%build
%{__autoconf}

export initdir=/etc/rc.d/init.d
%configure \
	--enable-force-shutdown=yes \
	--with-confdir=%{_sysconfdir} \
	--with-mapdir=%{_sysconfdir}

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

%preun
if [ "$1" = "0" ]; then
	%service autofs stop
	/sbin/chkconfig --del autofs
fi

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
%attr(755,root,root) %{_sbindir}/automount
%dir /net
%dir %{_libdir}/autofs
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
%attr(755,root,root) %{_libdir}/autofs/mount_generic.so
%attr(755,root,root) %{_libdir}/autofs/mount_nfs.so
%attr(755,root,root) %{_libdir}/autofs/mount_nfs4.so
%attr(755,root,root) %{_libdir}/autofs/parse_hesiod.so
%attr(755,root,root) %{_libdir}/autofs/parse_sun.so
%{_mandir}/man[58]/*

%files ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/autofs_ldap_auth.conf
%attr(755,root,root) %{_libdir}/autofs/lookup_ldap.so
%attr(755,root,root) %{_libdir}/autofs/lookup_ldaps.so
