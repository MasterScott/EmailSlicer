Name: libpff
Version: 20180714
Release: 1
Summary: Library to access the Personal Folder File (OST, PAB and PST) format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libpff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
                  
                  

%description
Library to access the Personal Folder File (OST, PAB and PST) format

%package devel
Summary: Header files and libraries for developing applications for libpff
Group: Development/Libraries
Requires: libpff = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libpff.

%package python
Summary: Python 2 bindings for libpff
Group: System Environment/Libraries
Requires: libpff = %{version}-%{release} python
BuildRequires: python-devel

%description python
Python 2 bindings for libpff

%package python3
Summary: Python 3 bindings for libpff
Group: System Environment/Libraries
Requires: libpff = %{version}-%{release} python3
BuildRequires: python3-devel

%description python3
Python 3 bindings for libpff

%package tools
Summary: Several tools for reading Personal Folder Files (OST, PAB and PST)
Group: Applications/System
Requires: libpff = %{version}-%{release}

%description tools
Several tools for reading Personal Folder Files (OST, PAB and PST)

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpff.pc
%{_includedir}/*
%{_mandir}/man3/*

%files python
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files python3
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%files tools
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Apr 17 2019 Joachim Metz <joachim.metz@gmail.com> 20180714-1
- Auto-generated
