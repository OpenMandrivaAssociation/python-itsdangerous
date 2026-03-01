%global upstream_name itsdangerous

Name:           python-%{upstream_name}
Version:        2.2.0
Release:        1
Group:		Development/Python
Summary:        Python library for passing trusted data to untrusted environments
License:        BSD
URL:            https://pythonhosted.org/itsdangerous/
Source0:        https://files.pythonhosted.org/packages/source/i/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python-setuptools
BuildRequires:  python-devel

%description
Itsdangerous is a Python library for passing data through untrusted 
environments (for example, HTTP cookies) while ensuring the data is not 
tampered with.

Internally itsdangerous uses HMAC and SHA1 for signing by default and bases the 
implementation on the Django signing module. It also however supports JSON Web 
Signatures (JWS).

%files
%doc CHANGES.rst
%{python3_sitelib}/%{upstream_name}/*.py*
%{python3_sitelib}/%{upstream_name}/__pycache__
%{python3_sitelib}/%{upstream_name}*.dist-info
%{python3_sitelib}/itsdangerous/py.typed
