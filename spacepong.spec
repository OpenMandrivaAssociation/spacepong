Summary:	An innovative pong like game
Name:		spacepong
Version:	0.0.2
Release:	4
License:	GPLv2+
Group:		Games/Arcade
URL:		http://spacepong.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/spacepong/%{name}_%{version}-1.tar.bz2
BuildArch:	noarch
Requires:	pygame
BuildRequires:	imagemagick

%description
An innovative game that is controlled with the mouse.
Steer you spacecraft ball around the screen and pickup
speed by bouncing off the walls. The goal is to collect
a certain amount of space boxes in a short time

%prep 
%setup -q -n %{name}-%{version}
convert data/ship.png -size 48x48 ship-48x48.png

%build 
#no build, this is a python script

%install
%makeinstall_std datadir=%{_gamesdatadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications/

cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=arcade_section
Categories=Game;ArcadeGame;
Name=SpacePong
Comment=%{Summary}
EOF

install -m644 data/ship-small.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 data/ship.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 ship-48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%defattr(-,root,root,0755) 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{name}/data
%{_gamesbindir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
