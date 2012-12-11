# $Id: urpmc.cooker.spec,v 1.3 2003/07/16 04:24:25 breser Exp $
%define name urpmc
%define version 1.2
%define release %mkrel 11

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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-11mdv2010.0
+ Revision: 434587
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-10mdv2009.0
+ Revision: 261806
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-9mdv2009.0
+ Revision: 255257
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2-7mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill changelog left by repsys


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:08:35 (41203)
- rebuild && mkrel
- fix file location

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:04:45 (41202)
Import urpmc

* Thu Jan 22 2004 Pixel <pixel@mandrakesoft.com> 1.2-6mdk
- rebuild for auto requires

* Wed Sep 10 2003 Ben Reser <ben@reser.org> 1.2-5mdk
- Really fix the BuildRequires (we need perl-devel)

* Wed Sep 10 2003 Ben Reser <ben@reser.org> 1.2-4mdk
- Fix Build Requires (courtesy of slbd)
- Macroization.

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-3mdk
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- don't use PREFIX
- use %%makeinstall_std macro

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 1.2-2mdk
- Fix grammatical error in description (Adam Williamson)
- Fix perl requires to use epoch (fpons)
- Location of perllocal.pod moved rm the right file.

* Tue Jul 15 2003 Ben Reser <ben@reser.org> 1.2-1mdk
- Fix quoting of urpmi.update and urpmq commands so
  media with meta chars work (found by Hawkwind)
- Typos, formating, and general documentation cleanups.
- s/sources/media/; s/source/medium/; and get the plurals
  and signulars right on them. (trappist)
- Better error handling of synthesis media.

* Tue Jul 15 2003 Ben Reser <ben@reser.org> 1.1-1mdk
- Actually cleanup temp files.
- Handle hdlist and synthesis being out of sync better.
- Added spec files to the package
- make dist now uses bzip2 and produces the gpg deatched sig.

* Tue Jul 15 2003 Ben Reser <ben@reser.org> 1.0-1mdk
- Rebuild for cooker/different perl dependencies

* Tue Jul 15 2003 Ben Reser <ben@reser.org> 1.0-0.90mdk
- Initial release

