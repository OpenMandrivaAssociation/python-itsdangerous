%global upstream_name itsdangerous

Name:           python-%{upstream_name}
Version:        2.1.2
Release:        1
Group:		Development/Python
Summary:        Python library for passing trusted data to untrusted environments
License:        BSD
URL:            http://pythonhosted.org/itsdangerous/
Source0:        http://pypi.python.org/packages/source/i/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python-devel

%description
Itsdangerous is a Python library for passing data through untrusted 
environments (for example, HTTP cookies) while ensuring the data is not 
tampered with.

Internally itsdangerous uses HMAC and SHA1 for signing by default and bases the 
implementation on the Django signing module. It also however supports JSON Web 
Signatures (JWS).

%prep
%setup -q -n %{upstream_name}-%{version}
#rm -r *.egg-info
%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#%check
#PYTHONPATH=%{buildroot}%{python_sitelib} %{__python} tests.py

%files
%doc LICENSE.rst CHANGES.rst README.rst
%{python3_sitelib}/%{upstream_name}/*.py*
#{python3_sitelib}/%{upstream_name}/*/*.py*
%{python3_sitelib}/%{upstream_name}*.egg-info
%{python3_sitelib}/itsdangerous/py.typed
