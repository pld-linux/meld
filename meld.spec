# TODO: make pl translation, commit it to gnome repository
#       and attch pl.patch here ;)
#
Summary:	Visual diff and merge tool
Summary(pl):	Wizualne narzêdzie do ogl±dania i w³±czania zmian (diff)
Name:		meld
Version:	0.9.5
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	dc86bf6f5ed1887da6a28ac1d91eb78d
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-omf.patch
URL:		http://meld.sf.net/
BuildRequires:	python-pyorbit-devel >= 1.99.7
BuildRequires:	python-gnome-devel >= 1.99.18
BuildRequires:	python-pygtk-devel >= 1.99.18
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,postun):	desktop-file-utils
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 1.99.18
Requires:	python-gnome >= 1.99.18
Requires:	python-gnome-ui >= 1.99.18
Requires:	python-gnome-gconf >= 1.99.18
Requires:	python-pyorbit >= 1.99.18
Requires:	python-pygtk-glade >= 1.99.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%description -l pl
Meld to przeznaczone dla GNOME 2 wizualne narzêdzie do ogl±dania i
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/usr/bin/scrollkeeper-update -q
/usr/bin/update-desktop-database

%postun
if [ $1 = 0]; then
	umask 022
	/usr/bin/scrollkeeper-update -q
	/usr/bin/update-desktop-database
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS changelog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
