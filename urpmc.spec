Name:		urpmc
Summary:	User rpm change(s|log)
Version:	1.2
Release:	13
Source0:	http://ben.reser.org/mandrake/%{name}/%{name}-%{version}.tar.bz2
URL:		http://ben.reser.org/cvsweb/urpmc/
Group:		System/Configuration/Packaging
BuildArch:	noarch
License:	GPL
Requires:	perl >= 2:5.8.0
BuildRequires:	perl-devel >= 2:5.8.0

%description
urpmc will run urpmi.update on one or more media, get the list of packages
that an auto-select would install, and show the changelogs of those packages
from the hdlist.

This program should be suitable for adding to a cronjob so you can see what
updates you need to install and why.  Especially useful for cooker developers
so they can see what changes they are installing, not just the package names.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README Changes COPYING
%{_mandir}/man1/*
%{_bindir}/%{name}
