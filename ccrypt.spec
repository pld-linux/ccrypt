Summary:	Secure encryption and decryption of files and streams
Summary(pl):	Bezpieczne szyfrowanie i odszyfrowywanie plik�w i strumieni
Name:		ccrypt
Version:	1.2
Release:	1
License:	GPL
Group:          Applications/System
Group(de):      Applikationen/System
Group(pl):      Aplikacje/System
Source0:	http://ccrypt.sourceforge.net/download/%{name}-%{version}.tar.gz
URL:		http://ccrypt.sourceforge.net/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed to replace the standard unix crypt utility, which is
notorious for using a very weak encryption algorithm. ccrypt is based
on the Rijndael date for the Advanced Encryption Standard (AES). This
cipher is believed to provide very strong security.

%description -l pl
ccrypt jest narz�dziem do szyfrowania i odszyfrowywania plik�w oraz
strumieni. Zosta�o opracowane by zast�pi� standardowe narz�dzie
uniksowe crypt, kt�re u�ywa bardzo s�abego algorytmu szyfrowania.
ccrypt bazuje na Rijndael AES (Advanced Encryption Standard). Ten
szyfr jest uwa�any za daj�cy du�e bezpiecze�stwo.

%prep
%setup -q -n ccrypt-1.2

%build
./configure
%{__make}  CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/ccrypt	$RPM_BUILD_ROOT%{_bindir}
ln -sfn ccrypt 		$RPM_BUILD_ROOT%{_bindir}/ccat
ln -sfn ccrypt 		$RPM_BUILD_ROOT%{_bindir}/ccencrypt
ln -sfn ccrypt 		$RPM_BUILD_ROOT%{_bindir}/ccdecrypt
install doc/ccrypt.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf AUTHORS ChangeLog NEWS README doc/cypfaq01.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
