#
# Conditional build:
%bcond_without	tests	# unit tests

%define	pdir	Any
%define	pnam	Moose
Summary:	Any::Moose - use Moose or Mouse modules
Summary(pl.UTF-8):	Any::Moose - używanie modułów Moose lub Mouse
Name:		perl-Any-Moose
Version:	0.27
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Any/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c5d318ee105c3a556019da537df542f
URL:		https://metacpan.org/dist/Any-Moose
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Moose
#BuildRequires:	perl-MooseX-Types
BuildRequires:	perl-Mouse >= 0.40
#BuildRequires:	perl-MouseX-Types
BuildRequires:	perl-Test-Simple >= 0.88
%endif
# or perl-Moose
Requires:	perl-Mouse >= 0.40
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Any::Moose is deprecated. Please use Moo instead.

%description -l pl.UTF-8
Any::Moose jest przestarzały. Zamiast niego należy używać Moo.

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
%{perl_vendorlib}/Any/Moose.pm
%{_mandir}/man3/Any::Moose.3pm*
