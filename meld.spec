%include	/usr/lib/rpm/macros.python
Summary:	Visual diff and merge tool
Summary(pl):	Wizualne narzêdzie do ogl±dania i w³±czania zmian (diff)
Name:		meld
Version:	0.9.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	1dfd1205c405bc263fc49ea1d92d47bf
Patch0:		%{name}-desktop.patch
URL:		http://meld.sf.net/
BuildRequires:	python-pyorbit-devel >= 1.99.7
BuildRequires:	python-gnome-devel >= 1.99.18
BuildRequires:	python-pygtk-devel >= 1.99.18
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk >= 1.99.18
Requires:	python-gnome >= 1.99.18
Requires:	python-pyorbit >= 1.99.18
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/glade2/pixmaps,%{_datadir}/%{name}/manual,%{_desktopdir},%{_pixmapsdir}}

install %{name} *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install glade2/*.glade* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2
install glade2/pixmaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/glade2/pixmaps
install glade2/pixmaps/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/meld.png
install manual/*.html $RPM_BUILD_ROOT%{_datadir}/%{name}/manual
install manual/*.css $RPM_BUILD_ROOT%{_datadir}/%{name}/manual
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

echo "exec %{_datadir}/%{name}/%{name} \$*" >$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO.txt changelog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/glade2
%{_datadir}/%{name}/manual
%{_desktopdir}/*
%{_pixmapsdir}/*
