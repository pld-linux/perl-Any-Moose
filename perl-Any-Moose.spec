#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Any
%define	pnam	Moose
%include	/usr/lib/rpm/macros.perl
Summary:	use Moose or Mouse modules
Name:		perl-Any-Moose
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b03e7c3e2593005105aa8347f9571d5
URL:		http://search.cpan.org/dist/Any-Moose/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mouse >= 0.21
%endif
Requires:	perl-Mouse >= 0.21
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Actual documentation is forthcoming, once we solidify all the bits of
the API. The examples above are very likely to continue working.

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
%{perl_vendorlib}/Any/*.pm
%{_mandir}/man3/*
