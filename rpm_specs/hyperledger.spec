Name:           hyperledger
Version:        master
Release:        1%{?dist}
Summary:        A blockchain project

License:        APACHE-2
URL:            https://github.com/hyperledger/fabric

BuildRequires:  git, golang >= 1.6, gcc-c++, snappy-devel, zlib-devel, bzip2-devel
Requires:       libstdc++, glibc, gcc-c++, gcc, snappy, zlib, bzip2
ExclusiveArch:  x86_64

#Source0:        fabric.tar.gz


%description
The fabric is an implementation of blockchain technology,
leveraging familiar and proven technologies.

#%prep
#%setup -q

%build
export GOPATH=%{_builddir}
mkdir -p $GOPATH/src/github.com/hyperledger
cd $GOPATH/src/github.com/hyperledger
git clone --single-branch -b master --depth 1 http://gerrit.hyperledger.org/r/fabric
cd $GOPATH/src/github.com/hyperledger/fabric/peer
CGO_CFLAGS=" " CGO_LDFLAGS="-lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go install
go clean
cd $GOPATH/src/github.com/hyperledger/fabric/membersrvc
CGO_CFLAGS=" " CGO_LDFLAGS="-lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go install
go clean

%install
mkdir -p %{buildroot}/opt/gopath
cp -rp bin pkg src %{buildroot}/opt/gopath/


%files
%defattr(-,root,root)
/opt/gopath/*


%changelog
* Tue Jul 26 2016 George Bolo <gbolo@linuxctl.com> 4.1-1
- Spec file for hyperledger git tested on centos 7
