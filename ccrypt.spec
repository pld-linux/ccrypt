Summary:	Secure encryption and decryption of files and streams
Name:		ccrypt
Version:	1.2
Release:	1
Copyright:	GNU Public License
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
install doc/ccrypt.1	$RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf AUTHORS ChangeLog COPYING INSTALL NEWS README doc/cypfaq01.txt
%files
%defattr(644,root,root,755)
%doc *.gz doc/*gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%clean
rm -rf $RPM_BUILD_ROOT
