# $Id: urpmc.cooker.spec,v 1.3 2003/07/16 04:24:25 breser Exp $
%define name urpmc
%define version 1.2
%define release %mkrel 9

Name:		%{name}
Summary: 	User rpm change(s|log)
Version: 	%{version}
Release:	%{release}
Source: 	http://ben.reser.org/mandrake/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
URL: 		http://ben.reser.org/cvsweb/urpmc/
Group: 		System/Configuration/Packaging
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std
%{__rm} -rf $RPM_BUILD_ROOT/%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README Changes COPYING
%{_mandir}/man1/*
%{_bindir}/%{name}

