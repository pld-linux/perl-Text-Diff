#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Diff
Summary:	Text::Diff - perform diffs on files and record sets
Summary(pl.UTF-8):	Text::Diff - wyszukiwanie różnic między plikami i zbiorami rekordów
Name:		perl-Text-Diff
Version:	1.44
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f0bcd24b64b50a29ad1cf997c2247e9
URL:		http://search.cpan.org/dist/Text-Diff/
%if %{with tests}
BuildRequires:	perl-Algorithm-Diff >= 1.19
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
diff() provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is
better integrated with Perl and available on all platforms. It is
often faster than shelling out to a system's diff executable for small
files, and generally slower on larger files.

%description -l pl.UTF-8
Funkcja diff() udostępnia podstawowy zbiór usług podobnych do
narzędzia GNU diff. Daleko jej do pełnej funkcjonalności GNU diffa,
ale jest lepiej zintegrowana z Perlem i dostępna na wszystkich
platformach. Jest przeważnie szybsza niż uruchamianie polecenia
systemowego w przypadku małych plików, a wolniejsza dla dużych plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/Diff.pm
%{perl_vendorlib}/Text/Diff
%{_mandir}/man3/Text::Diff*.3pm*
