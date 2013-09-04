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
Version: 	4.3.0
Release: 	1
Source0: 	https://www.enthought.com/repo/ets/ets-%{version}.tar.gz
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
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx

%description
The Enthought Tool Suite (ETS) is a collection of Python components
developed by Enthought and its partners to construct custom scientific
applications. 

This package contains the dependencies for installing all of the
components comprised by the suite.

%prep 
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
%__python setup.py build_docs

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst build/docs/html
%_bindir/%{module}*
%py_sitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814657
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-2
+ Revision: 745815
- Fix traitsui version dependency.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745693
- Update to 4.1.0.

* Tue Oct 18 2011 Lev Givon <lev@mandriva.org> 4.0.0-6
+ Revision: 705303
- Fix requires again.

* Tue Oct 18 2011 Lev Givon <lev@mandriva.org> 4.0.0-5
+ Revision: 705118
- Fix typo in requires.

* Mon Oct 17 2011 Lev Givon <lev@mandriva.org> 4.0.0-4
+ Revision: 705010
- Fix pythonegg version.

* Fri Sep 02 2011 Lev Givon <lev@mandriva.org> 4.0.0-3
+ Revision: 697902
- Update chaco dependency to 4.0.1.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-2
+ Revision: 689218
- Obsolete python-enthought-enthoughtbase.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689153
- import python-ets



