#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-jupyter_core
Version  : 5.3.1
Release  : 82
URL      : https://files.pythonhosted.org/packages/9e/53/f27bd74ceaa672a1ce17b4b2bee93c0742ca00cb9f540ec4fa60cf7319b5/jupyter_core-5.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/53/f27bd74ceaa672a1ce17b4b2bee93c0742ca00cb9f540ec4fa60cf7319b5/jupyter_core-5.3.1.tar.gz
Summary  : Jupyter core package. A base package on which Jupyter projects rely.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_core-bin = %{version}-%{release}
Requires: pypi-jupyter_core-license = %{version}-%{release}
Requires: pypi-jupyter_core-python = %{version}-%{release}
Requires: pypi-jupyter_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(traitlets)
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Core
[![Build Status](https://github.com/jupyter/jupyter_core/actions/workflows/test.yml/badge.svg?query=branch%3Amain++)](https://github.com/jupyter/jupyter_core/actions/workflows/test.yml/badge.svg?query=branch%3Amain++)
[![Documentation Status](https://readthedocs.org/projects/jupyter-core/badge/?version=latest)](http://jupyter-core.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the pypi-jupyter_core package.
Group: Binaries
Requires: pypi-jupyter_core-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_core package.


%package license
Summary: license components for the pypi-jupyter_core package.
Group: Default

%description license
license components for the pypi-jupyter_core package.


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
Requires: pypi(platformdirs)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-jupyter_core package.


%prep
%setup -q -n jupyter_core-5.3.1
cd %{_builddir}/jupyter_core-5.3.1
pushd ..
cp -a jupyter_core-5.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686785889
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH=%{buildroot}}$(python -c "import sys; print(sys.path[-1])")
pytest || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_core
cp %{_builddir}/jupyter_core-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_core/48e819ce4dc25dbb0fa0dfe362ff76776469bbc4 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter
/usr/bin/jupyter-migrate
/usr/bin/jupyter-troubleshoot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_core/48e819ce4dc25dbb0fa0dfe362ff76776469bbc4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
