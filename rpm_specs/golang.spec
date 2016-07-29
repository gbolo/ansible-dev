Name:           golang
Version:        1.6
Release:        1%{?dist}
Summary:        An open source programming language

License:        BSD
URL:            https://golang.org

#BuildRequires:  gcc-c++, snappy-devel, zlib-devel, bzip2-devel
#Requires:       libstdc++, glibc, gcc-c++, gcc, snappy, zlib, bzip2
ExclusiveArch:  x86_64

Source0:        https://storage.googleapis.com/golang/go%{version}.linux-amd64.tar.gz

%define debug_package %{nil}
%define _use_internal_dependency_generator 0
%define __find_requires %{nil}

%description
Go is an open source programming language that makes it
easy to build simple, reliable, and efficient software.

%prep
%setup -q -c

%build


%install
mkdir -p %{buildroot}/etc/profile.d
echo 'export PATH=$PATH:/usr/local/go/bin' > %{buildroot}/etc/profile.d/go-bin.sh
mkdir -p %{buildroot}/usr/local
cp -rp go %{buildroot}/usr/local/


%files
%defattr(-,root,root)
/usr/*
/etc/*


%changelog
* Tue Jul 27 2016 George Bolo <gbolo@linuxctl.com>
- Spec file for golang tested on centos 7
