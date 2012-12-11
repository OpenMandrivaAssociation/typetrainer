%define debug_package %{nil}
Summary:        Typing skills training utility
Name:           typetrainer
Version:        0.3.1
Release:        2
# generated with python setup.py sdist
# git commit e997d831dbd35a2927d37a03f5e293b4e5ce48ad
Source0:        %{name}-%{version}.tar.gz
Url:            https://github.com/baverman/typetrainer
License:	MIT
Group:		Text tools
BuildRequires: python
BuildRequires: python-setuptools
Requires:       python pygtk2.0

%description
This small utility allows you to grow your typing skills in soft and
non-annoying manner. It tries to behave closely to proprietary VerseQ
application -- adaptive typing tutor which dynamically changes exercises to
help trainee to learn hard places thoroughly.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%files
%doc README.rst LICENSE
%_bindir/typetrainer
%{py_sitedir}/%{name}/
%{py_sitedir}/%{name}-%{version}-py%{py_ver}.egg-info


%changelog
* Sat Jan 29 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.3.1-1mdv2011.0
+ Revision: 633933
- Imported to cooker
- Created package structure for typetrainer.

