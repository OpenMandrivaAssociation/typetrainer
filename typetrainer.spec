Summary:        Typing skills training utility
Name:           typetrainer
Version:        0.3.1
Release:        %mkrel 1
# generated with python setup.py sdist
# git commit e997d831dbd35a2927d37a03f5e293b4e5ce48ad
Source0:        %{name}-%{version}.tar.gz
Url:            https://github.com/baverman/typetrainer
License:	MIT
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc README.rst LICENSE
%_bindir/typetrainer
%{py_sitedir}/%{name}/
%{py_sitedir}/%{name}-%{version}-py%{pyver}.egg-info
