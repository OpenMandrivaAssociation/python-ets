%define module	ets

Summary:	Enthought Tool Suite
Name: 	 	python-%{module}
Version: 	4.4.4
Release: 	2
Source0: 	https://pypi.python.org/packages/source/e/ets/ets-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/ets/
BuildArch: 	noarch
Obsoletes:	python-enthought
Obsoletes:	python-enthought-enthoughtbase
BuildRequires: 	python-setuptools >= 0.6c8
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx
BuildSystem:	python

%patchlist
ets-4.3.0.test_fix.patch
python-ets-python3.patch

%description
The Enthought Tool Suite (ETS) is a collection of Python components
developed by Enthought and its partners to construct custom scientific
applications. 

This package contains the dependencies for installing all of the
components comprised by the suite.

%build -a
python setup.py build_docs

%files
%doc *.txt *.rst build/docs/html
%_bindir/%{module}*
%py_sitedir/%{module}*
