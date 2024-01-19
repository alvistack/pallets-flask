# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-flask
Epoch: 100
Version: 2.3.3
Release: 1%{?dist}
BuildArch: noarch
Summary: A simple framework for building complex web applications
License: BSD-3-Clause
URL: https://github.com/pallets/flask/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Flask is a lightweight WSGI web application framework. It is designed to
make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around Werkzeug and
Jinja and has become one of the most popular Python web application
frameworks.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-flask
Summary: A simple framework for building complex web applications
Requires: python3
Requires: python3-blinker >= 1.6.2
Requires: python3-click >= 8.1.3
Requires: python3-importlib-metadata >= 3.6.0
Requires: python3-itsdangerous >= 2.1.2
Requires: python3-Jinja2 >= 3.1.2
Requires: python3-werkzeug >= 2.3.0
Provides: python3-flask = %{epoch}:%{version}-%{release}
Provides: python3dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flask) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-flask
Flask is a lightweight WSGI web application framework. It is designed to
make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around Werkzeug and
Jinja and has become one of the most popular Python web application
frameworks.

%files -n python%{python3_version_nodots}-flask
%license LICENSE.rst
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-flask
Summary: A simple framework for building complex web applications
Requires: python3
Requires: python3-blinker >= 1.6.2
Requires: python3-click >= 8.1.3
Requires: python3-importlib-metadata >= 3.6.0
Requires: python3-itsdangerous >= 2.1.2
Requires: python3-Jinja2 >= 3.1.2
Requires: python3-werkzeug >= 2.3.0
Provides: python3-flask = %{epoch}:%{version}-%{release}
Provides: python3dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flask) = %{epoch}:%{version}-%{release}

%description -n python3-flask
Flask is a lightweight WSGI web application framework. It is designed to
make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around Werkzeug and
Jinja and has become one of the most popular Python web application
frameworks.

%files -n python3-flask
%license LICENSE.rst
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-flask
Summary: A simple framework for building complex web applications
Requires: python3
Requires: python3-blinker >= 1.6.2
Requires: python3-click >= 8.1.3
Requires: python3-importlib-metadata >= 3.6.0
Requires: python3-itsdangerous >= 2.1.2
Requires: python3-jinja2 >= 3.1.2
Requires: python3-werkzeug >= 2.3.0
Provides: python3-flask = %{epoch}:%{version}-%{release}
Provides: python3dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flask) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flask = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flask) = %{epoch}:%{version}-%{release}

%description -n python3-flask
Flask is a lightweight WSGI web application framework. It is designed to
make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around Werkzeug and
Jinja and has become one of the most popular Python web application
frameworks.

%files -n python3-flask
%license LICENSE.rst
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
