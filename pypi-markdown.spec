#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-markdown
Version  : 3.3.7
Release  : 85
URL      : https://files.pythonhosted.org/packages/d6/58/79df20de6e67a83f0d0bbfe6c19bb82adf68cdf362885257eb01099f930a/Markdown-3.3.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/58/79df20de6e67a83f0d0bbfe6c19bb82adf68cdf362885257eb01099f930a/Markdown-3.3.7.tar.gz
Summary  : Python implementation of Markdown.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-markdown-bin = %{version}-%{release}
Requires: pypi-markdown-license = %{version}-%{release}
Requires: pypi-markdown-python = %{version}-%{release}
Requires: pypi-markdown-python3 = %{version}-%{release}
Requires: pypi(importlib_metadata)
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
[Python-Markdown][]
===================
[![Build Status][build-button]][build]
[![Coverage Status][codecov-button]][codecov]
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]
[![BSD License][bsdlicense-button]][bsdlicense]
[![Code of Conduct][codeofconduct-button]][Code of Conduct]

%package bin
Summary: bin components for the pypi-markdown package.
Group: Binaries
Requires: pypi-markdown-license = %{version}-%{release}

%description bin
bin components for the pypi-markdown package.


%package license
Summary: license components for the pypi-markdown package.
Group: Default

%description license
license components for the pypi-markdown package.


%package python
Summary: python components for the pypi-markdown package.
Group: Default
Requires: pypi-markdown-python3 = %{version}-%{release}

%description python
python components for the pypi-markdown package.


%package python3
Summary: python3 components for the pypi-markdown package.
Group: Default
Requires: python3-core
Provides: pypi(markdown)

%description python3
python3 components for the pypi-markdown package.


%prep
%setup -q -n Markdown-3.3.7
cd %{_builddir}/Markdown-3.3.7
pushd ..
cp -a Markdown-3.3.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656387894
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-markdown
cp %{_builddir}/Markdown-3.3.7/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-markdown/686030b6b3298c011fe74266f0cde2d2c77f4a13
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown_py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-markdown/686030b6b3298c011fe74266f0cde2d2c77f4a13

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
