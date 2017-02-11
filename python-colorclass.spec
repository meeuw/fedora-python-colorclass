%global srcname colorclass
%global sum Yet another ANSI color text library for Python

Name:           python-%{srcname}
Version:        1.2.0
Release:        8%{?dist}
Summary:        Yet another ANSI color text library for Python

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/Robpol86/colorclass/blob/master/LICENSE

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel

%description
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%package -n python2-%{srcname}
Summary:        Yet another ANSI color text library for Python
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.


%package -n python3-%{srcname}
Summary:        Yet another ANSI color text library for Python
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%prep
%autosetup -n %{srcname}-%{version}
cp %{SOURCE1} .
rm -rf colorclass.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colorclass*
%{python3_sitelib}/__pycache__/colorclass.*

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 11 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-3
- Include changes from Julien's review #2 (Bugzilla #1258405)

* Tue Sep 08 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-2
- Include changes from Julien's review (Bugzilla #1258405)

* Mon Aug 31 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-1
- Initial rpm
