%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	A compilation of solitaire card games
Name:		aisleriot
Version:	3.2.2
Release:	1
License:	GPLv3+
Group:		Games/Other
Url:		http://live.gnome.org/Aisleriot
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# deb/ubuntu
Patch0:		aisleriot-3.2.2_format_not_a_string_literal.patch

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(guile-1.8)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(sm)

Conflicts:	gnome-games < 2.29.6

%description
Aisleriot (also known as Solitaire or sol) is a collection of card games
which are easy to play with the aid of a mouse. The rules for the games
have been coded for your pleasure in the GNOME scripting language (Scheme).

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-schemas-compile \
	--disable-schemas-install

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome
# https://bugzilla.redhat.com/show_bug.cgi?id=736523
echo "%%dir %%{_datadir}/help/C" >> aisleriot.lang
echo "%%{_datadir}/help/C/%%{name}" >> aisleriot.lang
for l in ca de el en_GB es eu fr gl oc ru sl sr sr@latin sv zh_CN; do
	echo "%%dir %%{_datadir}/help/$l"
	echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
done >> aisleriot.lang

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%attr(2555, root, games) %{_bindir}/sol
%{_libdir}/%{name}/
%{_datadir}/%{name}
%{_datadir}/applications/sol.desktop
%{_datadir}/applications/freecell.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_iconsdir}/*/*/*/gnome-aisleriot.*
%{_iconsdir}/*/*/*/gnome-freecell.*
%{_mandir}/man6/sol.*

