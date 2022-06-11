Name:		aisleriot
Summary:	A compilation of solitaire card games
License:	GPLv3+
Group:		Games/Cards
Version:	3.22.23
Release:	1
Url:		http://live.gnome.org/Aisleriot
#Source0:	http://download.gnome.org/sources/aisleriot/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Source0:	https://gitlab.gnome.org/GNOME/aisleriot/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(atomic_ops)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(guile-2.2)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: yelp-tools
BuildRequires: desktop-file-utils
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Svg)
BuildRequires: qt5-devel
BuildRequires: meson
BuildRequires: glibc-static-devel

Recommends:   pysol
Recommends:   PySolFC
Recommends:   PySolFC-cardsets
Recommends:   pysol-cardsets
Recommends:   libkdegames-common

%description
Aisleriot (also known as Solitaire or sol) is a collection of card games
which are easy to play with the aid of a mouse. The rules for the games
have been coded for your pleasure in the GNOME scripting language (Scheme).

%prep
%setup -q
%autopatch -p1

%build

%meson \
       -D theme_pysol=true \
       -D theme_pysol_path=%{_datadir}/PySolFC \
       -D theme_kde=true \
       -D theme_kde_path=%{_datadir}/apps/carddecks \
       -D theme_svg_qtsvg=true \
       -D theme_svg_rsvg=true
       
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/sol.desktop

%find_lang %{name} --with-gnome


%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING.* TODO
%{_bindir}/*
%{_libdir}/aisleriot
%{_libdir}/valgrind
%{_libexecdir}/aisleriot/
%{_datadir}/aisleriot
%{_datadir}/metainfo/sol.metainfo.xml
%{_datadir}/applications/sol.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_mandir}/man6/sol.6*
