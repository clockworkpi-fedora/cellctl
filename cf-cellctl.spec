Name:       cf-cellctl
Version:    1.0.0
Release:    1%{?dist}
Summary:    Control utility for the ClockworkPi uConsole cellular module.

License:    GPL-3.0-only
URL:        https://github.com/clockworkpi-fedora/cf-cellctl

Requires:   libgpiod-utils

BuildArch:  noarch

Source0:    %{name}-%{version}.tar.gz
#Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%description
Control utility for the ClockworkPi uConsole cellular module.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 src/cf-cellctl.sh %{buildroot}%{_bindir}/cf-cellctl

%check
sh -n %{buildroot}%{_bindir}/cf-cellctl

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed Nov 19 2025 David Goldstein 1.0.0-1
- Initial commit

