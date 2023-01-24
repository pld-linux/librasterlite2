%define		rel	1
Summary:	Library supporting rasters on DBMS
Summary(pl.UTF-8):	Biblioteka wspierająca przechowywanie rastrów w bazach danych
Name:		librasterlite2
Version:	1.1.0
%define	subver	beta1
Release:	0.%{subver}.%{rel}
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/librasterlite2-sources/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	39f6fe5348727920317c8037116c6766
URL:		https://www.gaia-gis.it/fossil/librasterlite2
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	curl-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	giflib-devel
BuildRequires:	libgeotiff-devel >= 1.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	lz4-devel
BuildRequires:	minizip-devel
BuildRequires:	openjpeg2-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires:	libgeotiff >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librasterlite2 is an open source library that stores and retrieves
huge raster coverages using a SpatiaLite DBMS.

%description -l pl.UTF-8
librasterlite2 to mająca otwarte źródła biblioteka przechowująca i
odtwarzająca duże pokrycia rastrowe przy użyciu silnika baz danych
SpatiaLite.

%package devel
Summary:	Header files for rasterlite2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rasterlite2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libspatialite-devel
Requires:	sqlite3-devel >= 3

%description devel
Header files for rasterlite2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki rasterlite2.

%package static
Summary:	Static rasterlite2 library
Summary(pl.UTF-8):	Statyczna biblioteka rasterlite2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static rasterlite2 library.

%description static -l pl.UTF-8
Statyczna biblioteka rasterlite2.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librasterlite2.la
# sqlite3 module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mod_rasterlite2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/rl2sniff
%attr(755,root,root) %{_bindir}/rl2tool
%attr(755,root,root) %{_bindir}/wmslite
%attr(755,root,root) %{_libdir}/librasterlite2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librasterlite2.so.1
%attr(755,root,root) %{_libdir}/mod_rasterlite2.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librasterlite2.so
%{_includedir}/rasterlite2
%{_pkgconfigdir}/rasterlite2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librasterlite2.a
