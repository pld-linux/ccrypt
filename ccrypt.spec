Summary:	Secure encryption and decryption of files and streams
Summary(pl):	Bezpieczne szyfrowanie i odszyfrowywanie plików i strumieni
Name:		ccrypt
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ccrypt/%{name}-%{version}.tar.gz
# Source0-md5:	ec5476db1833d56f55c714c749e9a2be
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://ccrypt.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed to replace the standard unix crypt utility, which is
notorious for using a very weak encryption algorithm. ccrypt is based
on the Rijndael date for the Advanced Encryption Standard (AES). This
cipher is believed to provide very strong security.

%description -l pl
ccrypt jest narzêdziem do szyfrowania i odszyfrowywania plików oraz
strumieni. Zosta³o opracowane by zast±piæ standardowe narzêdzie
uniksowe crypt, które u¿ywa bardzo s³abego algorytmu szyfrowania.
ccrypt bazuje na Rijndael AES (Advanced Encryption Standard). Ten
szyfr jest uwa¿any za daj±cy du¿e bezpieczeñstwo.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo ".so ccrypt.1." > $RPM_BUILD_ROOT%{_mandir}/man1/ccat.1
echo ".so ccrypt.1." > $RPM_BUILD_ROOT%{_mandir}/man1/ccdecrypt.1
echo ".so ccrypt.1." > $RPM_BUILD_ROOT%{_mandir}/man1/ccencrypt.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/cypfaq01.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
