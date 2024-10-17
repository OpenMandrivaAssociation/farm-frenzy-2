Name: farm-frenzy-2
Version: 1.0
Release: 3
# Tarball generated from installing the game available at the download
# URL by running
# WINEPREFIX=/usr/lib/games/Fram-Frenzy-2 wine farmfrenzy2_setup_full.exe
# cd /usr/lib/games/Farm-Frenzy-2
# remove-unnecessary-wine-bits
# cd ..
# tar cJf farm-frenzy-2.tar.xz Farm-Frenzy-2
Source0: farm-frenzy-2.tar.xz
# Tarball generated by running
# (after installing the game with wine as described above)
Source1: farm-frenzy-2-icons.tar.xz
Source2: winegame.c
# Used for creating source tarball, see above
Source3: remove-unnecessary-wine-bits
Summary: Farming game
URL: https://www.myplaycity.com/farm-frenzy-2/
License: Distributable
Group: Games/Arcade
ExclusiveArch: %{ix86} x86_64
%ifarch %{ix86}
Requires: wine
%else
Requires: wine32
# We need the 32bit version of ALSA's pulseaudio plugin
Requires: libalsa-plugins-pulseaudio
%endif

%description
Play Farm Frenzy 2 and experience all the pleasures of country life!
While playing the game you may really start thinking of moving by and
by to a village nearby! It is a teaser for city-dwellers and a relaxation
for native villagers.

You have lots of mini-missions: feed chickens, collect eggs, stock up your
warehouse and ship your goods off to markets. You need to produce 16 products
on your own and purchase 5 products in the city.

Deal with some 4 different domestic animals and make your business flourish!
Earn enough money to be able to upgrade your multiple buildings
(12 buildings all in all with 3 upgrades apiece!) and to buy new equipment
to manufacture the goods and please your consumers.

To provide better transportation of your goods to the markets at higher speeds,
upgrade the plane and the truck you have at your disposal. Download Farm
Frenzy 2 and start your country business!

You are the owner of a bakery, a confectionary, a cheese factory and 9 other
buildings that comprise your farm business. The only annoying feature that can
spoil your thoroughly designed business plans are the bears. This time you
have to face the risk of being looted by four different types of bears that
haunt your farm and turn your plans upside down.

Use cages to prevent them from doing harm to your business. Collect all the
19 awards and prove to be a perfect entrepreneur! With colorful 3D graphics,
heel-kicking music and hours of down-home gameplay, Farm Frenzy 2 offers a
bumper crop of fun! Play Farm Frenzy 2 right now!

%install
mkdir -p %{buildroot}%{_prefix}/lib/games
cd %{buildroot}%{_prefix}/lib/games
tar xf %{SOURCE0}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor
cd %{buildroot}%{_datadir}/icons/hicolor
tar xf %{SOURCE1}

mkdir -p %{buildroot}%{_bindir}
%__cc %{optflags} -DGAMEPATH=\"%{_prefix}/lib/games/Farm-Frenzy-2/dosdevices/c:/Program\ Files/MyPlayCity.com/Farm\ Frenzy\ 2\" -o %{buildroot}%{_bindir}/%{name} %{SOURCE2}

mkdir -p %{buildroot}%{_datadir}/applications
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Name=Farm Frenzy 2
Description=Farming Game
Exec=%{_bindir}/%{name}
Type=Application
StartupNotify=true
Icon=4D13_game_icon.0
EOF

%files
%attr(6755,root,root) %{_bindir}/%{name}
%dir %{_prefix}/lib/games/Farm-Frenzy-2
%attr(0664,root,games) %{_prefix}/lib/games/Farm-Frenzy-2/*.reg
%{_prefix}/lib/games/Farm-Frenzy-2/drive_c
%{_prefix}/lib/games/Farm-Frenzy-2/dosdevices
%{_prefix}/lib/games/Farm-Frenzy-2/.update-timestamp
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
