%define upstream_version 20100122

Summary: Mobile broadband provider database
Name: mobile-broadband-provider-info
Version: 1.%{upstream_version}
Release: 1%{?dist}
#
# Source from git://git.gnome.org/mobile-broadband-provider-info
# tarball built with:
#    ./autogen.sh --prefix=/usr
#    make distcheck
#
Source: mobile-broadband-provider-info-%{upstream_version}.tar.bz2
License: Public Domain
Group: System Environment/Base

BuildArch: noarch
URL: http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: libxml2

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains files necessary for
developing developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%configure
make %{?_smp_mflags}
make check

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc COPYING README
%attr(0644,root,root) %{_datadir}/%{name}/*
	
%files devel
%defattr(0644, root, root, 0755)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 22 2010 Dan Williams <dcbw@redhat.com> - 1.20100122-1
- Update to latest upstream release including:
- Cyprus, Austria, Ireland, Ukraine, Romainia, Cambodia (rh #530981), 
- Iraq, India, Sri Lanka, UK, Australia, Singapore,
- South Korea, Italy, United States, China (rh #517253), Nigeria,
- Tanzania, Germany, Qatar, Russia, and Finland (rh #528988)

* Fri Sep 18 2009 Dan Williams <dcbw@redhat.com> - 1.20090918-1
- Update to latest upstream release including:
- Algeria, Australia, Belarus, Belgium, Brazil
- Brunei, Bulgaria, Egypt, Finland, Ghana, Greece
- India, Italy, Kazakhstan, Korean CDMA operators
- Kuwait, Mali, Netherlands, Paraguay, Serbia
- Spain, Sweden, UK

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.20090707-3
- Add -devel sub-package with pkg-config file (#511318)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20090707-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 7 2009 Dan Williams <dcbw@redhat.com> - 1.20090707-1
- Update to latest upstream release including:
- T-Mobile USA
- Brazil
- Bangladesh
- Sweden
- Spain
- Moldova

* Tue Jun 3 2009 Dan Williams <dcbw@redhat.com> 0.20090602-2
- Package review fixes

* Tue Jun 2 2009 Dan Williams <dcbw@redhat.com> 0.20090602-1
- Initial version

