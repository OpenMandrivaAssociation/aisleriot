Name:		aisleriot
Summary:	A compilation of solitaire card games
License:	GPLv3+
Group:		Games/Cards
Version:	3.16.1
Release:	1
Url:		http://live.gnome.org/Aisleriot
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(guile-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: yelp-tools
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(Qt5Svg)

%description
Aisleriot (also known as Solitaire or sol) is a collection of card games
which are easy to play with the aid of a mouse. The rules for the games
have been coded for your pleasure in the GNOME scripting language (Scheme).

%prep
%setup -q

%build
%configure 	\
	--with-card-theme-formats=all \
	--with-kde-card-theme-path=%{_datadir}/apps/carddecks \
	--with-pysol-card-theme-path=%{_datadir}/PySolFC \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-static
    
%make V=1

%install
%makeinstall_std

desktop-file-validate %{buildroot}%{_datadir}/applications/sol.desktop

%find_lang %{name} --with-gnome



%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc AUTHORS
%license COPYING.GPL3 COPYING.LGPL3 COPYING.GFDL
%{_bindir}/*
%{_libdir}/aisleriot
%{_libexecdir}/aisleriot/
%{_datadir}/aisleriot
%{_datadir}/appdata/sol.appdata.xml
%{_datadir}/applications/sol.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/HighContrast/*/apps/*.svg
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_mandir}/man6/sol.6*
