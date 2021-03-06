%define realname openmsx

Name:           openttd-%{realname}
Version:        0.3.1
Release:        4
Summary:        OpenMSX music replacement set for OpenTTD

Group:          Games/Strategy
License:        GPLv2
URL:            http://dev.openttdcoop.org/projects/openmsx
Source0:        http://bundles.openttdcoop.org/openmsx/releases/%{version}/%{realname}-%{version}-source.tar.gz
# Mirror:
#Source0:        https://github.com/OpenTTD/OpenMSX/archive/%{version}/%{realname}-%{version}-source.tar.gz
Patch0:         openmsx-0.3.1-python3.patch

BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  python

%description
OpenMSX is an open source replacement for the original Transport Tycoon
Deluxe (TTD) music.

%prep
%autosetup -p1 -n %{realname}-%{version}-source

%build
%make_build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/openttd/gm
%make_install INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/gm

%files
%doc docs/*.txt
%{_gamesdatadir}/openttd/gm/%{realname}-%{version}
