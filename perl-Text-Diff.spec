#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Diff
Summary:	Text::Diff - perform diffs on files and record sets
Summary(pl):	Text::Diff - wyszukiwanie r�nic mi�dzy plikami i zbiorami rekord�w
Name:		perl-Text-Diff
Version:	0.35
Release:	4
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4931662ea353384dec2a54a71b26ee8c
URL:		http://search.cpan.org/dist/Text-Diff/
%if %{with tests}
BuildRequires:	perl-Algorithm-Diff
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

%description -l pl
Funkcja diff() udost�pnia podstawowy zbi�r us�ug podobnych do
narz�dzia GNU diff. Daleko jej do pe�nej funkcjonalno�ci GNU diffa,
ale jest lepiej zintegrowana z Perlem i dost�pna na wszystkich
platformach. Jest przewa�nie szybsza ni� uruchamianie polecenia
systemowego w przypadku ma�ych plik�w, a wolniejsza dla du�ych plik�w.

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
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/Diff
%{_mandir}/man3/*
