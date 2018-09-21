Name:		aisleriot
Summary:	A compilation of solitaire card games
License:	GPLv3+
Group:		Games/Cards
Version:	3.22.6
Release:	1
Url:		http://live.gnome.org/Aisleriot
Source0:	http://download.gnome.org/sources/aisleriot/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(guile-2.2)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: yelp-tools
BuildRequires: desktop-file-utils
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Svg)
BuildRequires: qt5-devel

%description
Aisleriot (also known as Solitaire or sol) is a collection of card games
which are easy to play with the aid of a mouse. The rules for the games
have been coded for your pleasure in the GNOME scripting language (Scheme).

%prep
%setup -q
%apply_patches

%build
export CXX="%__cxx -std=c++11"

%configure 	\
	--with-card-theme-formats=all \
	--with-kde-card-theme-path=%{_datadir}/apps/carddecks \
	--with-pysol-card-theme-path=%{_datadir}/PySolFC \
	--with-platform=gtk-only \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-static

%make V=1

%install
%makeinstall_std

desktop-file-validate %{buildroot}%{_datadir}/applications/sol.desktop

%find_lang %{name} --with-gnome


%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING.* ChangeLog NEWS TODO
%{_bindir}/*
%{_libdir}/aisleriot
%{_libdir}/valgrind
%{_libexecdir}/aisleriot/
%{_datadir}/aisleriot
%{_datadir}/metainfo/sol.appdata.xml
%{_datadir}/applications/sol.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_mandir}/man6/sol.6*
