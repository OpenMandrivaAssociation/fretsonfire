Summary:	Frets On Fire
Name:		fretsonfire
Version:	1.3.110
Release:	2
Group:		Games/Arcade
License:	GPLv2
URL:		https://fretsonfire.sourceforge.net/
Source:		FretsOnFire-%{version}.tar.gz
Patch0:		fretsonfire-1.3.110-credits_music.patch
Patch1:		fretsonfire-1.3.110-datapath.patch
Patch2:		fretsonfire-1.3.110-font-revert.patch
Patch3:		fretsonfire-1.3.110-fonts_lower_cpu.patch
Patch4:		fretsonfire-1.3.110-keep_sound_when_failed.patch
Patch5:		fretsonfire-1.3.110-typeerror.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	python-numpy
Requires:	python-imaging
Requires:	python-opengl
Requires:	pygame

%description
Frets on Fire is a game of musical skill and fast fingers.
The aim of the game is to play guitar with the keyboard as
accurately as possible.

%prep
%setup -q -n Frets\ on\ Fire-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
chmod 644 copying.txt

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
mkdir -p %{buildroot}%{_gamesbindir}

install -D -m 0644 data/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -r data %{buildroot}%{_gamesdatadir}/%{name}/
cp -r src %{buildroot}%{_gamesdatadir}/%{name}/

#Menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Frets On Fire
Comment=Game of Musical Skill and Fast Fingers
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

#Executable
cat > %{buildroot}%{_gamesbindir}/%{name}<<EOF
#!/bin/sh
cd /
cd %{_gamesdatadir}/%{name}/src
python ./FretsOnFire.py
EOF

chmod 0755 %{buildroot}%{_gamesbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc copying.txt readme.txt
%attr(755,root,root) %{_gamesbindir}/fretsonfire
%{_gamesdatadir}/fretsonfire
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Mon Dec 05 2011 Andrey Bondrov <abondrov@mandriva.org> 1.3.110-1
+ Revision: 737797
- imported package fretsonfire

