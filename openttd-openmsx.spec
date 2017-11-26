%define realname openmsx

Name:           openttd-%{realname}
Version:        0.3.1
Release:        3
Summary:        OpenMSX music replacement set for OpenTTD

Group:          Games/Strategy
License:        GPLv2
URL:            http://dev.openttdcoop.org/projects/openmsx
Source0:        http://bundles.openttdcoop.org/openmsx/releases/%{version}/%{realname}-%{version}-source.tar.gz
BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  python
Conflicts:      openttd < 1.0.0-2mdv

%description
OpenMSX is an open source replacement for the original Transport Tycoon
Deluxe (TTD) music.

%prep
%setup -q -n %{realname}-%{version}-source

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_gamesdatadir}/openttd/gm
%make install INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/gm

%check
%make check

%files
%defattr(644,root,root,755)
%doc docs/*.txt
%{_gamesdatadir}/openttd/gm/%{realname}-%{version}
