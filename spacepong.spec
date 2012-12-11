%define name	spacepong
%define version	0.0.2
%define release	3
%define	Summary	An innovative pong like game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version} 
Release:	%mkrel %{release}
License:	GPLv2+
Group:		Games/Arcade
URL:		http://spacepong.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/spacepong/%{name}_%{version}-1.tar.bz2
BuildArch:	noarch
Requires:	pygame
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,0755) 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesdatadir}/%{name}/data
%{_gamesbindir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.0.2-3mdv2010.0
+ Revision: 434012
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.0.2-2mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 25 2008 Funda Wang <fundawang@mandriva.org> 0.0.2-2mdv2008.1
+ Revision: 158020
- fix desktop entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.0.2-1mdv2008.1
+ Revision: 135454
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import spacepong


* Wed Aug 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.0.2-1mdk
- import rpm with some adaptations (nice third party spec! :)

* Tue Aug 09 2005 Dovix <dovix2003@yahoo.com> 0.0.2-0.1.102mdk
- New release
- Use mkrel
- Fix some errors reported by rpmlint

* Fri Jul 29 2005 Dovix <dovix2003@yahoo.com> 0.0.1-1mdk
- Initial version
