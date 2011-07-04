# $Id: lightlang.spec $
# Authority: akdengi
# Upstream: lightlang.org.ru

%define version 0.0.1
%define	rel	1
%define release %mkrel %{rel}

%{?dist: %{expand: %%define %dist 1}}

Summary: Dictionary for LightLang
Name: lightlang-dict-other
Version:	%{version}
Release:	%{release}
License: GPL
Group: Office
URL: http://lightlang.org.ru

Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: lightlang

%description
Dictionary for LightLang
Словари для LightLang

%prep
%setup

%{__rm} -rf %{buildroot}
mkdir %{buildroot}
mkdir %{buildroot}/usr
mkdir %{buildroot}/usr/share
mkdir %{buildroot}/usr/share/sl
mkdir %{buildroot}/usr/share/sl/dicts
cp ./* %{buildroot}/usr/share/sl/dicts

%build


%clean
%{__rm} -rf %{buildroot}



%files
%defattr(-, root, root, 0755)

%{_datadir}/sl/dicts/*

