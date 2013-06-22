#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Message
%include	/usr/lib/rpm/macros.perl
Summary:	HTTP::Message - HTTP style message
Summary(pl.UTF-8):	HTTP::Message - komunikacja w stylu HTTP
Name:		perl-HTTP-Message
Version:	6.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e563ac516e28d33f65bc0f295f625f85
URL:		http://search.cpan.org/dist/HTTP-Message/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Encode >= 2.21
BuildRequires:	perl-Encode-Locale >= 1
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl-HTTP-Date >= 6
BuildRequires:	perl-MIME-Base64 >= 2.1
BuildRequires:	perl-IO-Compress >= 2.021
BuildRequires:	perl-IO-HTML
BuildRequires:	perl-URI >= 1.10
BuildRequires:	perl-LWP-MediaTypes >= 6
%endif
Requires:	perl-Encode >= 2.21
Requires:	perl-Encode-Locale >= 1
Requires:	perl-HTTP-Date >= 6
Requires:	perl-MIME-Base64 >= 2.1
Requires:	perl-URI >= 1.10
Requires:	perl-LWP-MediaTypes >= 6
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP-Message distribution contains classes useful for representing
the messages passed in HTTP style communication. These are classes
representing requests (HTTP::Request), responses (HTTP::Response) and
the headers (HTTP::Headers) contained within them.

%description -l pl.UTF-8
Pakiet HTML-Message zawiera klasy do reprezentacji komunikatów
przekazywanych w komunikacji w stylu HTTP. Zawiera klasy
reprezentujące żądania (HTTP::Request), odpowiedzi (HTTP::Response) i
nagłówki (HTTP::Headers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Config.pm
%{perl_vendorlib}/HTTP/Headers.pm
%{perl_vendorlib}/HTTP/Headers
%{perl_vendorlib}/HTTP/Message.pm
%{perl_vendorlib}/HTTP/Request.pm
%{perl_vendorlib}/HTTP/Request
%{perl_vendorlib}/HTTP/Response.pm
%{perl_vendorlib}/HTTP/Status.pm
%{_mandir}/man3/HTTP::Config.3pm*
%{_mandir}/man3/HTTP::Headers*.3pm*
%{_mandir}/man3/HTTP::Message.3pm*
%{_mandir}/man3/HTTP::Request*.3pm*
%{_mandir}/man3/HTTP::Response.3pm*
%{_mandir}/man3/HTTP::Status.3pm*
