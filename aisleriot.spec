%define	Werror_cflags	%nil
%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		aisleriot
Version:	3.4.1
Release:	1
Url:		http://live.gnome.org/Aisleriot
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Summary:	A compilation of solitaire card games
License:	GPLv3+
Group:		Games/Other
Conflicts:	gnome-games < 2.29.6-2
BuildRequires:	pkgconfig(cairo) >= 1.10.0
BuildRequires:	pkgconfig(gconf-2.0) >= 2.0
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(guile-2.0) >= 2.0.0
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	pkgconfig(sm)
BuildRequires:	intltool
BuildRequires:	yelp-tools
BuildRequires:	itstool
BuildRequires:	gnome-doc-utils
BuildRequires:	docbook-dtd41-sgml
#BuildRequires:	guile

# For autoreconf, due to Patch0
BuildRequires:	gettext-devel

%description
Aisleriot (also known as Solitaire or sol) is a collection of card games
which are easy to play with the aid of a mouse. The rules for the games
have been coded for your pleasure in the GNOME scripting language (Scheme).

%prep
%setup -q
autoreconf -fi

%build
%configure2_5x \
	--disable-schemas-compile \
	--disable-schemas-install \
	--disable-static
%make V=1

%install
%makeinstall_std

%find_lang %{name} --with-help

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%attr(2555, root, games) %{_bindir}/sol
%{_libdir}/%{name}/
%{_libdir}/valgrind/aisleriot.supp
%{_datadir}/applications/sol.desktop
%{_datadir}/applications/freecell.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_iconsdir}/*/*/*/gnome-aisleriot.*
%{_iconsdir}/*/*/*/gnome-freecell.*
%{_mandir}/man6/sol.*
%{_datadir}/%{name}

