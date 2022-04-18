#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_core
Version  : 4.10.0
Release  : 61
URL      : https://files.pythonhosted.org/packages/91/5d/746dd5b904854043f99e72a22c69a2e9b3eb0ade2adc2b288e666ffa816f/jupyter_core-4.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/5d/746dd5b904854043f99e72a22c69a2e9b3eb0ade2adc2b288e666ffa816f/jupyter_core-4.10.0.tar.gz
Summary  : Jupyter core package. A base package on which Jupyter projects rely.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_core-bin = %{version}-%{release}
Requires: pypi-jupyter_core-python = %{version}-%{release}
Requires: pypi-jupyter_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(traitlets)
BuildRequires : pypi-pytest

%description
# Jupyter Core
Core common functionality of Jupyter projects.
This package contains base application classes and configuration inherited by other projects.
It doesn't do much on its own.

%package bin
Summary: bin components for the pypi-jupyter_core package.
Group: Binaries

%description bin
bin components for the pypi-jupyter_core package.


%package python
Summary: python components for the pypi-jupyter_core package.
Group: Default
Requires: pypi-jupyter_core-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_core package.


%package python3
Summary: python3 components for the pypi-jupyter_core package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_core)
Requires: pypi(pywin32)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-jupyter_core package.


%prep
%setup -q -n jupyter_core-4.10.0
cd %{_builddir}/jupyter_core-4.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650294516
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter
/usr/bin/jupyter-migrate
/usr/bin/jupyter-troubleshoot

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
