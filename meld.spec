# TODO: make pl translation, commit it to gnome repository
#       and attach pl.patch here ;)
#
Summary:	Visual diff and merge tool
Summary(pl.UTF-8):	Wizualne narzędzie do oglądania i włączania zmian (diff)
Name:		meld
Version:	1.5.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/GNOME/sources/meld/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	387f24c936e2a433ac3dedd298008675
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-GNUmakefile.patch
Patch2:		%{name}-glob.patch
URL:		http://meld.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-modules >= 2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires:	hicolor-icon-theme
Requires:	python-pygobject >= 2.16
Requires:	python-pygtk-gtk >= 2.14
Suggests:	python-gtksourceview2 >= 2.4
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%patch2 -p1

%build
%{__make} \
	prefix=%{_prefix} \
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

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
