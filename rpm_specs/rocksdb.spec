Name:           rocksdb
Version:        4.1
Release:        1%{?dist}
Summary:        A Persistent Key-Value Store for Fast Storage Environments

License:        BSD
URL:            https://github.com/facebook/rocksdb.git

BuildRequires:  gcc-c++, snappy-devel, zlib-devel, bzip2-devel
ExclusiveArch:  x86_64

Source0:        https://github.com/facebook/%{name}/archive/v%{version}.tar.gz


%description
A library that provides an embeddable, persistent key-value store for fast storage

%package devel
Summary: Development files for rocksdb
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for rocksdb

%prep
%setup -q

%build
# make PORTABLE - https://github.com/facebook/rocksdb/issues/690
PORTABLE=1 make shared_lib

%install
INSTALL_PATH=%{buildroot}/usr make install-shared
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib64/librocksdb.so*

%files devel
/usr/lib64/librocksdb.so
/usr/include/*


%changelog
* Mon Jul 25 2016 George Bolo <gbolo@linuxctl.com> 4.1-1
- Spec file for rocksdb 4.1 tested on centos 7
