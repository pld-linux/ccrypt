Summary:	Secure encryption and decryption of files and streams
Summary(pl.UTF-8):	Bezpieczne szyfrowanie i odszyfrowywanie plików i strumieni
Name:		ccrypt
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/ccrypt/%{name}-%{version}.tar.gz
# Source0-md5:	262573b04416b3b947f0d38807ec5246
URL:		http://ccrypt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed to replace the standard Unix crypt utility, which is
notorious for using a very weak encryption algorithm. ccrypt is based
on the Rijndael date for the Advanced Encryption Standard (AES). This
cipher is believed to provide very strong security.

%description -l pl.UTF-8
ccrypt jest narzędziem do szyfrowania i odszyfrowywania plików oraz
strumieni. Zostało opracowane by zastąpić standardowe narzędzie
uniksowe crypt, które używa bardzo słabego algorytmu szyfrowania.
ccrypt bazuje na Rijndael AES (Advanced Encryption Standard). Ten
szyfr jest uważany za dający duże bezpieczeństwo.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/cypfaq01.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
