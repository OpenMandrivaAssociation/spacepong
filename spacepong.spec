%define name	spacepong
%define version	0.0.2
%define release	1
%define	Summary	An innovative pong like game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version} 
Release:	%mkrel %{release}
License:	GPL
Group:		Games/Arcade
URL:		http://spacepong.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/spacepong/%{name}_%{version}-1.tar.bz2
BuildArch:	noarch
Requires:	pygame
BuildRequires:	ImageMagick

%description
An innovative game that is controlled with the mouse.
Steer you spacecraft ball around the screen and pickup
speed by bouncing off the walls. The goal is to collect
a certain amount of space boxes in a short time

%description -l he_IL
משחק תוצרת כחול לבן, העיקרון דיי פשוט :צריך לשלוט
בחללית הקטנה בעזרת העכבר (וזה לא פשוט כי החללית
נסחפת) ולאסוף חבילות מטען בחלל. צריך גם להיזהר לא
להתנגש במטאורים ובמוקשים ולעמוד במגבלות הזמן

%prep 
%setup -q -n %{name}-%{version}
convert data/ship.png -size 48x48 ship-48x48.png

%build 
#no build, this is a python script

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std datadir=%{_gamesdatadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/

cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}	
Icon=arcade_section		
Categories=Game;ArcadeGame;	
Name=SpacePong	
Comment=%{Summary}
EOF

install -m644 data/ship-small.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 data/ship.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 ship-48x48.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean 
rm -rf $RPM_BUILD_ROOT 

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755) 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{name}/data
%{_gamesbindir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

