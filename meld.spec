# TODO: make pl translation, commit it to gnome repository
#       and attch pl.patch here ;)
#
Summary:	Visual diff and merge tool
Summary(pl):	Wizualne narzêdzie do ogl±dania i w³±czania zmian (diff)
Name:		meld
Version:	1.1.4
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	e780a8f67183acf7f51b13aa4a62ac85
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%description -l pl
Meld to przeznaczone dla GNOME wizualne narzêdzie do ogl±dania i
w³±czania zmian (w formacie diff). Integruje siê szczególnie dobrze z
CVS. Przegl±darka ró¿nic pozwala modyfikowaæ pliki w miejscu
(dynamicznie uaktualniaæ), a ¶rodkowa kolumna pokazuje szczegó³owe
zmiany i pozwala na w³±czanie. Na marginesach jest pokazane po³o¿enie
zmian w celu ³atwej nawigacji. Jest dostêpny tak¿e interfejs z
zak³adkami, pozwalaj±cy na otwieranie wielu plików diff naraz.

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

rm -r $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py

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
