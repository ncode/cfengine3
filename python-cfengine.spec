%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname cfengine3
%define srcname python-cfengine

Name:           python-%{pkgname}
Version:        0.1
Release:        1%{?dist}
Summary:        Python CFEngine3 Module Protocol
Group:          Development/Libraries

License:        GPL
URL:            https://github.com/ncode/cfengine3
Source0:        %{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-devel
Requires:       python
BuildArch:      noarch

%description
A simple way to extend your cfengine3 using python.

%prep
%setup -q -n %{pkgname}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/*
%exclude %{python_sitelib}/cfengine3/*.pyc
%exclude %{python_sitelib}/cfengine3/*.pyo

%changelog
* Mon Jun 11 2011 Luiz Viana <luiz.viana@locaweb.com.br>  - 0.1-1
- Initial package
