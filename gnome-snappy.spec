# NOTE: upstream package name in GNOME is snappy, but this name is already occupied in PLD
# by Google snappy compression library.
Summary:	Snappy media player
Summary(pl.UTF-8):	Odtwarzacz multimedialny Snappy
Name:		gnome-snappy
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/snappy/1.0/snappy-%{version}.tar.xz
# Source0-md5:	17598504ba57d4d21382faa1038476d9
URL:		https://wiki.gnome.org/Apps/Snappy
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gst-devel >= 2.0.0
BuildRequires:	clutter-gtk-devel >= 1.0.2
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.5.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires:	clutter >= 1.12.0
Requires:	clutter-gst >= 2.0.0
Requires:	clutter-gtk >= 1.0.2
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snappy is an open source media player that gathers the power and
flexibility of gstreamer inside the comfort of a minimalistic clutter
interface.

%description -l pl.UTF-8
Snappy to mający otwarte źródła odtwarzacz multimedialny, łączący siłę
i elastyczność gstreamera z komfortem minimalnego interfejsu opartego
na bibliotece clutter.

%prep
%setup -q -n snappy-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS ToDo
%attr(755,root,root) %{_bindir}/snappy
%{_datadir}/snappy
%{_desktopdir}/snappy.desktop
%{_iconsdir}/hicolor/*/apps/snappy.png
