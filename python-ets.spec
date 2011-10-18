%define module	ets
%define name	python-%{module}
%define version 4.0.0
%define release %mkrel 5

Summary:	Enthought Tool Suite
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
Patch0:		pythonegg-version-4.0.0.patch
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://code.enthought.com/projects/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Obsoletes:	python-enthought
Obsoletes:	python-enthought-enthoughtbase
Requires: 	python-apptools == 4.0.0
Requires: 	python-blockcanvas == 4.0.0
Requires:	python-chaco == 4.0.1
Requires:	python-codetools == 4.0.0
Requires: 	python-enable == 4.0.0
Requires: 	python-envisage == 4.0.0
Requires: 	python-etsdevtools == 4.0.0
Requires: 	python-graphcanvas == 4.0.0
Requires: 	python-mayavi == 4.0.0
Requires: 	python-pyface == 4.0.0
Requires: 	python-scimath == 4.0.0
Requires: 	python-traits == 4.0.0
Requires: 	python-traitsui == 4.0.0
BuildRequires: 	python-setuptools >= 0.6c8

%description
The Enthought Tool Suite (ETS) is a collection of Python components
developed by Enthought and its partners to construct custom scientific
applications. 

This package contains the dependencies for installing all of the
components comprised by the suite.

%prep 
%setup -q -n %{module}-%{version}
%patch0 -p0

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst
