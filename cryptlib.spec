Summary:	Peter Gutmann's general purpose encryption library
Summary(pl):	Biblioteka kryptograficzna ogólnego przeznaczenia Petera Gutmanna
Name:		cryptlib
Version:	3.22
Release:	1
License:	sleepycat
Group:		Libraries
Source0:	ftp://ftp.franken.de/pub/crypt/cryptlib/cl322.zip
# Source0-md5:	0944963faae4566f54aeb45c6e803142
URL:		http://www.cs.auckland.ac.nz/~pgut001/cryptlib/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cryptlib encryption library provides an easy-to-use interface
which allows even inexperienced crypto programmers to easily add
strong encryption and authentication services to their software. The
library contains DES, triple DES, IDEA, MDC/SHS, RC2, RC4, RC5, SAFER,
SAFER-SK, Blowfish, and Blowfish-SK conventional encryption, MD2, MD4,
MD5, RIPEMD-160 and SHA hash algorithms, and Diffie-Hellman, DSA, and
RSA public-key encryption.

%description -l pl
Biblioteka kryptograficzna cryptlib udostêpnia ³atwy w u¿yciu
interfejs pozwalaj±cy nawet niedo¶wiaczonym programistom kryptografii
³atwo dodawaæ do swoich programów us³ugi kryptograficzne i
uwierzytelnienia. Biblioteka zawiera szyfry konwencjonalne DES, 3DES,
IDEA, MDC/SHS, RC2, RC4, RC5, SAFER, SAFER-SK, Blowfish i Blowfish-SK,
algorytmy skrótu MD2, MD4, MD5, RIPEMD-160 i SHA oraz szyfry klucza
publicznego Diffie-Hellmana, DSA i RSA.

%package devel
Summary:	Header file for cryptlib library
Summary(pl):	Plik nag³ówkowy biblioteki cryptlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header file for developing applications that use the cryptlib
cryptography library.

%description devel -l pl
Plik nag³ówkowy do tworzenia aplikacji korzystaj±cych z biblioteki
kryptograficznej cryptlib.

%package static
Summary:	Static cryptlib library
Summary(pl):	Statyczna biblioteka cryptlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cryptlib library.

%description static -l pl
Statyczna biblioteka cryptlib.

%prep
%setup -q -T -c
unzip -L -a %{SOURCE0}

%build
%{__make} \
	CMDC="%{rpmcflags}"
%{__make} shared \
	CMDC="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install cryptlib.h $RPM_BUILD_ROOT%{_includedir}
install libcl.a $RPM_BUILD_ROOT%{_libdir}
install libcl.so.3.2.2 $RPM_BUILD_ROOT%{_libdir}
ln -sf libcl.so.3.2.2 $RPM_BUILD_ROOT%{_libdir}/libcl.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcl.so.3.2.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcl.so
%{_includedir}/cryptlib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcl.a
