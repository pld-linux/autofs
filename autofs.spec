# TODO:
# - change /net to something FHS-compliant ?
# - build of ldap-related things has some errors
Summary:	autofs daemon
Summary(de.UTF-8):	autofs daemon
Summary(es.UTF-8):	Servidor autofs
Summary(fr.UTF-8):	démon autofs
Summary(pl.UTF-8):	Demon autofs
Summary(pt_BR.UTF-8):	Servidor autofs
Summary(tr.UTF-8):	autofs sunucu süreci
Name:		autofs
Version:	5.0.2
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-%{version}.tar.bz2
# Source0-md5:	fd56817cba70814753bc98f5fb7f23ec
Source1:	%{name}.init
Source2:	%{name}-auto.master
Source3:	%{name}-auto.media
Source4:	%{name}-auto.net
Source5:	%{name}.sysconfig
Patch0:		%{name}-open_max.patch
Patch1:		%{name}-hesiod-includes.patch
## Official patches:
Patch10:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-krb5-include.patch
Patch11:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-bad-proto-init.patch
Patch12:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-missing-multi-support.patch
Patch13:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-multi-nsswitch-lookup.patch
Patch14:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-consistent-random-selection-option-name.patch
Patch15:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-offset-dir-create.patch
Patch16:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-quote-exports.patch
Patch17:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-hi-res-time.patch
Patch18:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-quoted-slash-alone.patch
Patch19:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-dnattr-parse.patch
Patch20:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-nfs-version-in-get-supported-ver-and-cost.patch
Patch21:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-instance-stale-mark.patch
Patch22:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-largefile-dumbness.patch
Patch23:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-dont-fail-on-empty-master.patch
Patch24:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-ldap-percent-hack.patch
Patch25:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-mount-nfs-nosymlink.patch
Patch26:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-dont-fail-on-empty-master-fix.patch
Patch27:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-default-nsswitch.patch
Patch28:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-ldap-schema-discovery.patch
Patch29:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-random-selection-fix.patch
Patch30:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-timeout-option-parse-fix.patch
Patch31:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-ldap-check-star.patch
Patch32:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-ldap-schema-discovery-fix.patch
Patch33:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-ldap-schema-discovery-config-update.patch
Patch34:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-ldap-search-basedn-list.patch
Patch35:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-libxml2-workaround.patch
Patch36:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-reread-config-on-hup.patch
Patch37:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-multiple-server-selection-option.patch
Patch38:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-foreground-logging.patch
Patch39:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-cleanup-krb5-comment.patch
Patch40:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-submount-deadlock.patch
Patch41:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-ferror-check.patch
Patch42:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-autofs-5-typo.patch
Patch43:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-swallow-null-macro.patch
Patch44:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-remove-unsed-export-validation-code.patch
Patch45:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-dynamic-logging.patch
Patch46:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-recursive-loopback-mounts.patch
Patch47:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-log-map-reload.patch
Patch48:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-basedn-with-spaces.patch
Patch49:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-dynamic-logging-fixes.patch
Patch50:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-basedn-with-spaces-fix.patch
Patch51:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-check-mtab-updated.patch
Patch52:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-basedn-with-spaces-fix-2.patch
Patch53:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-check-auto_master.patch
Patch54:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-ldap-schema-discovery-fix-2.patch
Patch55:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-negative-timeout-update.patch
Patch56:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-large-groups.patch
Patch57:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-report-failed-lookups.patch
Patch58:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-dynamic-logging-non-sasl.patch
Patch59:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-check-mtab-updated-fix.patch
Patch60:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-singleton-host-list.patch
Patch61:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-start-pipe-buff-size.patch
Patch62:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-fix-off-by-one-lookup.patch
Patch63:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-improve-server-unavail.patch
Patch64:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-add-multiple-server-selection-option-fix.patch
Patch65:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-external-cred-cache.patch
Patch66:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-percent-hack-fix.patch
Patch67:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-quote-exports-fix.patch
Patch68:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-hosts-nosuid-default.patch
Patch69:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-quote-exports-fix-fix.patch
Patch70:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-quell-mount-module-message.patch
Patch71:	ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/%{name}-5.0.2-improve-server-unavail-fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
BuildRequires:	krb5-devel
BuildRequires:	openldap-devel >= 2.4.6
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

#Official patches:
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
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1

%build
#chmod a+w configure
#%{__aclocal}
#%{__autoconf}
%configure

%{__make} \
	initdir=/etc/rc.d/init.d \
	CC="%{__cc}" \
	DAEMON_CFLAGS="%{rpmcflags}"

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
mv $RPM_BUILD_ROOT/etc/auto.smb $RPM_BUILD_ROOT%{_sysconfdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/auto.{home,var,tmp}

# Do some cleanups:
rm -f $RPM_BUILD_ROOT/etc/auto.{master,misc,net}

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.home
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.master
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.media
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.net
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.smb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.tmp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/auto.var
%attr(754,root,root) %config /etc/rc.d/init.d/autofs
%attr(755,root,root) %{_sbindir}/automount
%dir /net
%dir %{_libdir}/autofs
%attr(755,root,root) %{_libdir}/autofs/mount_*
%attr(755,root,root) %{_libdir}/autofs/parse_*
%attr(755,root,root) %{_libdir}/autofs/lookup_[!l]*
%{_mandir}/man[58]/*

%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/autofs/lookup_ldap.so
