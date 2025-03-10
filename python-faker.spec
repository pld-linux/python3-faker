#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Faker - Python package that generates fake data for you
Summary(pl.UTF-8):	Faker - pakiet Pythona generujący fałszywe dane
Name:		python-faker
# keep 3.x here for python2 support
Version:	3.0.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Faker/
Source0:	https://files.pythonhosted.org/packages/source/F/Faker/Faker-%{version}.tar.gz
# Source0-md5:	bcf900b630d836649175d1ac5ddab949
URL:		https://pypi.org/project/Faker/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-dateutil >= 2.4
BuildRequires:	python-freezegun
BuildRequires:	python-ipaddress
BuildRequires:	python-mock
BuildRequires:	python-pytest
BuildRequires:	python-random2
BuildRequires:	python-six >= 1.10
BuildRequires:	python-text-unidecode >= 1.3
BuildRequires:	python-ukpostcodeparser
BuildRequires:	python-validators
%endif
%endif
%if %{with python3}
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
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-faker
Summary:	Faker - Python package that generates fake data for you
Summary(pl.UTF-8):	Faker - pakiet Pythona generujący fałszywe dane
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-faker
Faker is a Python package that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML
documents, fill-in your persistence to stress test it, or anonymize
data taken from a production service, Faker is for you.

%description -n python3-faker -l pl.UTF-8
Faker to pakiet Pythona generujący fałszywe dane. Jest to przydatne,
kiedy potrzebujemy uruchomić bazę danych, stworzyć dobrze wyglądający
dokument XML, wypełnić dane do testów albo zanonimozować dane pobrane
z usługi produkcyjnej.

%prep
%setup -q -n Faker-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/faker{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/faker{,-3}
ln -sf faker-3 $RPM_BUILD_ROOT%{_bindir}/faker
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/faker-2
%{py_sitescriptdir}/faker
%{py_sitescriptdir}/Faker-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-faker
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/faker
%attr(755,root,root) %{_bindir}/faker-3
%{py3_sitescriptdir}/faker
%{py3_sitescriptdir}/Faker-%{version}-py*.egg-info
%endif
