%define module	ets
%define name	python-%{module}
%define version 4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/ets/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Obsoletes:	python-enthought
Obsoletes:	python-enthought-enthoughtbase
Requires: 	python-apptools == 4.1.0
Requires: 	python-blockcanvas == 4.0.1
Requires:	python-chaco == 4.2.0
Requires:	python-codetools == 4.0.0
Requires: 	python-enable == 4.2.0
Requires:	python-enaml == 0.2.0
Requires: 	python-envisage == 4.2.0
Requires: 	python-etsdevtools == 4.0.0
Requires: 	python-graphcanvas == 4.0.0
Requires: 	python-mayavi == 4.2.0
Requires: 	python-pyface == 4.2.0
Requires: 	python-scimath == 4.1.0
Requires: 	python-traits == 4.2.0
Requires: 	python-traitsui == 4.2.0
BuildRequires: 	python-setuptools >= 0.6c8
BuildRequires:	python-sphinx

%description
The Enthought Tool Suite (ETS) is a collection of Python components
developed by Enthought and its partners to construct custom scientific
applications. 

This package contains the dependencies for installing all of the
components comprised by the suite.

%prep 
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd docs
make html
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst docs/build/html
%_bindir/%{module}*
%py_sitedir/%{module}*
