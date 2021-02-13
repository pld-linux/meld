Summary:	Visual diff and merge tool
Summary(pl.UTF-8):	Wizualne narzędzie do oglądania i włączania zmian (diff)
Name:		meld
Version:	3.20.3
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/GNOME/sources/meld/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	28bd16508e9c966d04184c16046cbadb
Patch0:		%{name}-desktop.patch
Patch2:		%{name}-install.patch
URL:		http://meld.sourceforge.net/
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# for versions see bin/meld /check_requirements
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.48
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.48
Requires:	gtk+3 >= 3.20
Requires:	gtksourceview3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	pango >= 1:1.26
Requires:	python3-modules >= 1:3.3
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.14
BuildArch:	noarch
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
%patch2 -p1

cp -p meld/vc/COPYING COPYING.vc
cp -p meld/vc/README README.vc

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install install_data \
	--no-compile-schemas \
	--no-update-icon-cache

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS COPYING.vc README.vc
%attr(755,root,root) %{_bindir}/meld
%{py3_sitescriptdir}/meld-%{version}-py*.egg-info
%dir %{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}/*.py
%{py3_sitescriptdir}/%{name}/__pycache__
%dir %{py3_sitescriptdir}/%{name}/matchers
%{py3_sitescriptdir}/%{name}/matchers/*.py
%{py3_sitescriptdir}/%{name}/matchers/__pycache__
%dir %{py3_sitescriptdir}/%{name}/ui
%{py3_sitescriptdir}/%{name}/ui/*.py
%{py3_sitescriptdir}/%{name}/ui/__pycache__
%dir %{py3_sitescriptdir}/%{name}/vc
%{py3_sitescriptdir}/%{name}/vc/*.py
%{py3_sitescriptdir}/%{name}/vc/__pycache__
%{_iconsdir}/hicolor/16x16/actions/meld-change-*.png
%{_iconsdir}/hicolor/*x*/apps/meld-version-control.png
%{_iconsdir}/hicolor/*x*/apps/org.gnome.meld.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.meld.svg
%{_iconsdir}/HighContrast/scalable/apps/org.gnome.meld.svg
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%{_datadir}/metainfo/org.gnome.meld.appdata.xml
%{_datadir}/mime/packages/org.gnome.meld.xml
%{_desktopdir}/org.gnome.meld.desktop
%{_mandir}/man1/meld.1*
