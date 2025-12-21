Name:		calc_files
Version:	1.0
Release:	1%{?dist}
Summary:	Script to calculate files in the /etc directory
License:	MIT
URL:		https://github.com/kiril-vasylenko/sys-prog
BuildArch:	noarch
Requires:	bash findutils coreutils
Source0:	%{name}-%{version}.tar.gz

%description
This package contains a simple script that calculates the number of files in the /etc directory.

%prep
%setup -q

%build

%install
install -D -m 0755 calc_files.sh %{buildroot}%{_bindir}/calc_files

%files
%{_bindir}/calc_files

%changelog
* Sun Dec 21 2025 Kiril Vasylenko <vasylenko.k123@gmail.com> - 1.0-1
- Initial build
