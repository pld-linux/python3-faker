#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Faker - Python package that generates fake data for you
Summary(pl.UTF-8):	Faker - pakiet Pythona generujący fałszywe dane
Name:		python3-faker
Version:	37.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Faker/
Source0:	https://files.pythonhosted.org/packages/source/F/Faker/faker-%{version}.tar.gz
# Source0-md5:	10698ac88368efa4d507fa69020b5a3e
URL:		https://pypi.org/project/Faker/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-dateutil >= 2.4
BuildRequires:	python3-freezegun
BuildRequires:	python3-pytest
BuildRequires:	python3-random2
BuildRequires:	python3-six >= 1.10
BuildRequires:	python3-text-unidecode >= 1.3
BuildRequires:	python3-ukpostcodeparser
BuildRequires:	python3-validators
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faker is a Python package that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML
documents, fill-in your persistence to stress test it, or anonymize
data taken from a production service, Faker is for you.

%description -l pl.UTF-8
Faker to pakiet Pythona generujący fałszywe dane. Jest to przydatne,
kiedy potrzebujemy uruchomić bazę danych, stworzyć dobrze wyglądający
dokument XML, wypełnić dane do testów albo zanonimozować dane pobrane
z usługi produkcyjnej.

%prep
%setup -q -n faker-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/faker{,-3}
ln -sf faker-3 $RPM_BUILD_ROOT%{_bindir}/faker

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.rst LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/faker
%attr(755,root,root) %{_bindir}/faker-3
%{py3_sitescriptdir}/faker
%{py3_sitescriptdir}/Faker-%{version}-py*.egg-info
