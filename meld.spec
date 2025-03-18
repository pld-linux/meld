Summary:	Visual diff and merge tool
Summary(pl.UTF-8):	Wizualne narzędzie do oglądania i włączania zmian (diff)
Name:		meld
Version:	3.22.3
Release:	4
License:	GPL v2+
Group:		Applications/Text
Source0:	https://download.gnome.org/sources/meld/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	8dc9da40caa2a0fd1097af77d3b87abd
Patch0:		%{name}-desktop.patch
Patch2:		%{name}-install.patch
URL:		http://meldmerge.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.48
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	gtksourceview4-devel >= 4.0.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pycairo-devel >= 1.15.0
BuildRequires:	python3-pygobject3-devel >= 3.30
# ensure distutils.command.build.{Build -> build} rename (see distutils patch)
BuildRequires:	python3-setuptools >= 1:60
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# for versions see bin/meld /check_requirements
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.48
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.48
Requires:	gtk+3 >= 3.20
Requires:	gtksourceview4 >= 4.0.0
Requires:	hicolor-icon-theme
Requires:	pango >= 1:1.26
Requires:	python3-modules >= 1:3.6
Requires:	python3-pycairo >= 1.15.0
Requires:	python3-pygobject3 >= 3.30
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
%patch -P 0 -p1
%patch -P 2 -p1

cp -p meld/vc/COPYING COPYING.vc
cp -p meld/vc/README README.vc

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{name}/vc/{COPYING,README}

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
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Meld.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Meld-symbolic.svg
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%{_datadir}/metainfo/org.gnome.Meld.appdata.xml
%{_datadir}/mime/packages/org.gnome.Meld.xml
%{_desktopdir}/org.gnome.Meld.desktop
%{_mandir}/man1/meld.1*
