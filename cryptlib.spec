Summary:	Peter Gutmann's general purpose encryption library
Name:		cryptlib
Version:	3.22
Release:	1
License:	sleepycat
URL:		http://www.cs.auckland.ac.nz/~pgut001/cryptlib/
Source0:	ftp://ftp.franken.de/pub/crypt/cryptlib/cl322.zip
# Source0-md5:	0944963faae4566f54aeb45c6e803142
Group:		Libraries
BuildRequires:	unzip
Provides:	libcl.so
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cryptlib encryption library provides an easy-to-use interface
which allows even inexperienced crypto programmers to easily add
strong encryption and authentication services to their software. The
library contains DES, triple DES, IDEA, MDC/SHS, RC2, RC4, RC5, SAFER,
SAFER-SK, Blowfish, and Blowfish-SK conventional encryption, MD2, MD4,
MD5, RIPEMD-160 and SHA hash algorithms, and Diffie-Hellman, DSA, and
RSA public-key encryption.


%package devel
Summary:	Header file and static library for cryptlib
Group:		Development/Libraries
Requires:	cryptlib
Provides:	libcl.a 

%description devel
The header files and libraries for developing applications that use
the cryptlib cryptography library.

%prep
%setup -q -T -c
unzip -L -a $RPM_SOURCE_DIR/cl322.zip

%build
%{__make} CMDC="$RPM_OPT_FLAGS"
%{__make} shared CMDC="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/lib
install -d $RPM_BUILD_ROOT%{_includedir}
install cryptlib.h $RPM_BUILD_ROOT%{_includedir}
install libcl.a $RPM_BUILD_ROOT%{_prefix}/lib/libcl.a
install libcl.so.3.2.2 $RPM_BUILD_ROOT%{_prefix}/lib/libcl.so.3.2.2
ln -sf libcl.so.3.2.2 $RPM_BUILD_ROOT%{_prefix}/lib/libcl.so

%files
%defattr(644,root,root,755)
%{_prefix}/lib/libcl.so
%attr(755,root,root) %{_prefix}/lib/libcl.so.3.2.2

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/libcl.a
%{_includedir}/cryptlib.h

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
