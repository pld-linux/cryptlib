#
%define		libver	3.3.0
#
Summary:	Peter Gutmann's general purpose encryption library
Summary(pl.UTF-8):	Biblioteka kryptograficzna ogólnego przeznaczenia Petera Gutmanna
Name:		cryptlib
Version:	3.3.1
Release:	0.1
License:	sleepycat
Group:		Libraries
Source0:	ftp://ftp.franken.de/pub/crypt/cryptlib/cl331.zip
# Source0-md5:	3e93e5aa0b33fb1d5b05b099f01e0afe
URL:		http://www.cs.auckland.ac.nz/~pgut001/cryptlib/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:  rpm-pythonprov
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	libcl.so

%description
The cryptlib encryption library provides an easy-to-use interface
which allows even inexperienced crypto programmers to easily add
strong encryption and authentication services to their software. The
library contains DES, triple DES, IDEA, MDC/SHS, RC2, RC4, RC5, SAFER,
SAFER-SK, Blowfish, and Blowfish-SK conventional encryption, MD2, MD4,
MD5, RIPEMD-160 and SHA hash algorithms, and Diffie-Hellman, DSA, and
RSA public-key encryption.

%description -l pl.UTF-8
Biblioteka kryptograficzna cryptlib udostępnia łatwy w użyciu
interfejs pozwalający nawet niedoświaczonym programistom kryptografii
łatwo dodawać do swoich programów usługi kryptograficzne i
uwierzytelnienia. Biblioteka zawiera szyfry konwencjonalne DES, 3DES,
IDEA, MDC/SHS, RC2, RC4, RC5, SAFER, SAFER-SK, Blowfish i Blowfish-SK,
algorytmy skrótu MD2, MD4, MD5, RIPEMD-160 i SHA oraz szyfry klucza
publicznego Diffie-Hellmana, DSA i RSA.

%package devel
Summary:	Header file for cryptlib library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki cryptlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header file for developing applications that use the cryptlib
cryptography library.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia aplikacji korzystających z biblioteki
kryptograficznej cryptlib.

%package static
Summary:	Static cryptlib library
Summary(pl.UTF-8):	Statyczna biblioteka cryptlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cryptlib library.

%description static -l pl.UTF-8
Statyczna biblioteka cryptlib.

%package -n python-cryptlib
Summary:	Python bindings for cryptlib
Summary(pl.UTF-8):	Wiązania języka Python do biblioteki cryptlib
Group:		Libraries/Python
Requires:	python >= 1:2.4

%description -n python-cryptlib
Python bindings for cryptlib library.

%description -n python-cryptlib -l pl.UTF-8
Wiązania języka Python do biblioteki cryptlib.

%prep
%setup -q -T -c
unzip -L -a %{SOURCE0}

sed -i -e 's/ -O3 / %{rpmcflags} /' makefile

%build
%{__make} \
	CC="%{__cc}"

%{__make} shared \
	CC="%{__cc}"

ln -sf libcl.so.%{libver} libcl.so

cd bindings
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{py_sitedir}}

install cryptlib.h $RPM_BUILD_ROOT%{_includedir}
install libcl.a $RPM_BUILD_ROOT%{_libdir}
install libcl.so.%{libver} $RPM_BUILD_ROOT%{_libdir}
ln -s %{_libdir}/libcl.so.%{libver} $RPM_BUILD_ROOT%{_libdir}/libcl.so

cd bindings
python setup.py install	\
	--optimize=2	\
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcl.so.%{libver}
%{_libdir}/libcl.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/cryptlib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcl.a

%files -n python-cryptlib
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
