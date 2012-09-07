Summary:	Python bindings for Evas library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Evas
Name:		python-evas
Version:	1.7.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	c3fda2025171f5e3d2bc224e8bae88e5
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	python-Cython >= 0.15.1
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	eina >= 1.7.0
Requires:	evas >= 1.7.0
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Evas library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Evas.

%package devel
Summary:	Python bindings for Evas library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Evas - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	evas-devel >= 1.7.0

%description devel
Python bindings for Evas library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Evas - pliki programistyczne.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/evas/c_evas.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/evas
%attr(755,root,root) %{py_sitedir}/evas/c_evas.so
%{py_sitedir}/evas/*.py[co]
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_includedir}/python-evas
%{_pkgconfigdir}/python-evas.pc
