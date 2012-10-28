Summary:	A library of functions for controlling audio CD-ROM players
Name:		libcdaudio
Version:	0.99.12p2
Release:	14
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/libcdaudio/%{name}-%{version}.tar.gz
# Source0-md5:	15de3830b751818a54a42899bd3ae72c
URL:		http://libcdaudio.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs. It also contains
functions for CDDB and CD Index lookup.

%package devel
Summary:	Header files and libraries for libcdaudio development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libcdaudio-devel package provides the header files and libraries
needed for libcdaudio development.

%prep
%setup -q

# automake 1.12.x fixes
sed -i -e "/AM_C_PROTOTYPES/d" configure.ac
sed -i -e "/AUTOMAKE_OPTIONS.*/d" Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libcdaudio-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/libcdaudio.m4
%{_pkgconfigdir}/*.pc

