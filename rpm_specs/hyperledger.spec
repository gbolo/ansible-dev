Name:           hyperledger-fabric
Version:        0.6_160919
Release:        1%{?dist}
Summary:        A blockchain project

License:        APACHE-2
URL:            https://www.hyperledger.org

BuildRequires:  gcc-c++, snappy-devel, zlib-devel, bzip2-devel
Requires:       snappy, zlib, bzip2, rocksdb
ExclusiveArch:  x86_64

#Source0:       fabric.tar.gz


%description
The fabric is an implementation of blockchain technology,
leveraging familiar and proven technologies.

%package devel
Summary: Development files for hyperledger

%description devel
Development files for hyperledger

%package peer
Summary: hyperledger fabric peer only

%description peer
hyperledger fabric peer only

%package membersrvc
Summary: hyperledger fabric membersrvc only

%description membersrvc
hyperledger fabric membersrvc only

#%prep
#%setup -q

%build

# PREPARE
export GOPATH=%{_builddir}
mkdir -p $GOPATH/src/github.com/hyperledger
cd $GOPATH/src/github.com/hyperledger
git clone --single-branch -b v0.6 --depth 1 http://gerrit.hyperledger.org/r/fabric

# BUILD
cd $GOPATH/src/github.com/hyperledger/fabric/peer
#sed -i 's/err = client.StartContainer(containerID, getDockerHostConfig())/err = client.StartContainer(containerID)/g' $GOPATH/src/github.com/hyperledger/fabric/core/container/dockercontroller/dockercontroller.go
CGO_CFLAGS=" " CGO_LDFLAGS="-lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go install
go clean
cd $GOPATH/src/github.com/hyperledger/fabric/membersrvc
CGO_CFLAGS=" " CGO_LDFLAGS="-lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go install
go clean

%install
mkdir -p %{buildroot}/opt/gopath
cp -rp bin pkg src %{buildroot}/opt/gopath/


%files devel
%defattr(-,root,root)
/opt/gopath/*

%files peer
%defattr(-,root,root)
/opt/gopath/bin/peer
/opt/gopath/src/github.com/hyperledger/fabric/peer/core.yaml
/opt/gopath/src/github.com/hyperledger/fabric/consensus/pbft/config.yaml

%files membersrvc
%defattr(-,root,root)
/opt/gopath/bin/membersrvc
/opt/gopath/src/github.com/hyperledger/fabric/membersrvc/membersrvc.yaml

%changelog
* Mon Sep 19 2016 George Bolo <gbolo@linuxctl.com>
 - split up hyperledger parts
* Mon Jul 25 2016 George Bolo <gbolo@linuxctl.com>
 - initial
