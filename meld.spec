# TODO: make pl translation, commit it to gnome repository
#       and attch pl.patch here ;)
#
Summary:	Visual diff and merge tool
Summary(pl.UTF-8):	Wizualne narzędzie do oglądania i włączania zmian (diff)
Name:		meld
Version:	1.1.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	a92e72a3b4392ee3e677720f9a75246f
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-GNUmakefile.patch
URL:		http://meld.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	python-gnome-devel >= 2.15.1
BuildRequires:	python-pyorbit-devel >= 2.14.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
%pyrequires_eq	python-libs
Requires:	python-gnome >= 2.15.1
Requires:	python-gnome-ui >= 2.15.1
Requires:	python-pygtk-glade >= 2:2.9.0
Requires:	python-pyorbit >= 2.14.0
Suggests:	python-gnome-desktop-gtksourceview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%description -l pl.UTF-8
Meld to przeznaczone dla GNOME wizualne narzędzie do oglądania i
włączania zmian (w formacie diff). Integruje się szczególnie dobrze z
CVS. Przeglądarka różnic pozwala modyfikować pliki w miejscu
(dynamicznie uaktualniać), a środkowa kolumna pokazuje szczegółowe
zmiany i pozwala na włączanie. Na marginesach jest pokazane położenie
zmian w celu łatwej nawigacji. Jest dostępny także interfejs z
zakładkami, pozwalający na otwieranie wielu plików diff naraz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# Nasty quickfix - some translations are broken for now
rm -f po/{hu,ja,ru}.po
%{__make} \
	prefix=/usr \
	libdir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{py_sitedir}

touch $RPM_BUILD_ROOT%{py_sitedir}/meld/__init__.py

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
rm -r $RPM_BUILD_ROOT%{_datadir}/application-registry

%py_postclean

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS changelog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/vc
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
