#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Diff
Summary:	Text::Diff - perform diffs on files and record sets
Summary(pl):	Text::Diff - wyszukiwanie ró¿nic miêdzy plikami i zbiorami rekordów
Name:		perl-Text-Diff
Version:	0.35
Release:	2
License:	GPL v2+/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4931662ea353384dec2a54a71b26ee8c
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Algorithm-Diff
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
diff() provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is
better integrated with Perl and available on all platforms. It is
often faster than shelling out to a system's diff executable for small
files, and generally slower on larger files.

%description -l pl
Funkcja diff() udostêpnia podstawowy zbiór us³ug podobnych do
narzêdzia GNU diff. Daleko jej do pe³nej funkcjonalno¶ci GNU diffa,
ale jest lepiej zintegrowana z Perlem i dostêpna na wszystkich
platformach. Jest przewa¿nie szybsza ni¿ uruchamianie polecenia
systemowego w przypadku ma³ych plików, a wolniejsza dla du¿ych plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
