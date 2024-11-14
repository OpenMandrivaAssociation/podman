%undefine _debugsource_packages

Name: podman
Version: 5.3.0
Release: 1
Source0: https://github.com/containers/podman/archive/refs/tags/v%{version}.tar.gz
Summary: Tool for managing OCI containers and pods
URL: https://github.com/containers/podman
License: Apache-2.0
Group: Servers
BuildRequires: golang
BuildRequires: man
BuildRequires: git-core
BuildRequires: pkgconfig(libbtrfsutil)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(gpgme)
Requires: conmon

%description
Podman (the POD MANager) is a tool for managing containers and images, volumes
mounted into those containers, and pods made from groups of containers.

Podman is based on libpod, a library for container lifecycle management that is
also contained in this repository. The libpod library provides APIs for
managing containers, pods, container images, and volumes.

%prep
%autosetup -p1

%build
%make_build BUILDTAGS="selinux seccomp" PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/podman
%{_bindir}/podman-remote
%{_bindir}/podmansh
%{_prefix}/lib/systemd/system-generators/podman-system-generator
%{_prefix}/lib/systemd/system/podman-auto-update.service
%{_prefix}/lib/systemd/system/podman-auto-update.timer
%{_prefix}/lib/systemd/system/podman-clean-transient.service
%{_prefix}/lib/systemd/system/podman-kube@.service
%{_prefix}/lib/systemd/system/podman-restart.service
%{_prefix}/lib/systemd/system/podman.service
%{_prefix}/lib/systemd/system/podman.socket
%{_prefix}/lib/systemd/user-generators/podman-user-generator
%{_prefix}/lib/systemd/user/podman-auto-update.service
%{_prefix}/lib/systemd/user/podman-auto-update.timer
%{_prefix}/lib/systemd/user/podman-clean-transient.service
%{_prefix}/lib/systemd/user/podman-kube@.service
%{_prefix}/lib/systemd/user/podman-restart.service
%{_prefix}/lib/systemd/user/podman-user-wait-network-online.service
%{_prefix}/lib/systemd/user/podman.service
%{_prefix}/lib/systemd/user/podman.socket
%{_prefix}/lib/tmpfiles.d/podman.conf
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/quadlet
%{_libexecdir}/podman/rootlessport
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/podman-rootless.7*
%{_mandir}/man7/podman-troubleshooting.7*
