#!/usr/bin/env sh
echo """
#####################                                         #####################
#####################                                         #####################
#####################       FEDORA KIONITE SETUP SCRIPT       #####################
#####################                                         #####################
#####################                                         #####################

Execute the scripts:
- Download
- Open the Terminal in its folder (cd PATH/TO/FOLDER or right-click in Dolphin)
- do "sudo chmod +x Fedora-Kionite-setupscript-part1.sh Fedora-Kionite-setupscript-part2.sh"
- do "sudo sh Fedora-Kionite-setupscript-part1.sh"


This script sets up all you really need to enjoy the unbreakable,
stable and secure experience of Fedora Kionite.

In the end you have to reboot, to apply changes when installing RPMs. Configure Waydroid in the second script.

1. removing unwanted apps
    - this has to be activated manually, as changing the tree have negative effects
    - Gwenview, replaced with XNView
    - Kmousetool
    - KMag
    - maybe the RPM Firefox if you choose so


2. Setting up Flatpak repositories (where you get your apps from)
    - Flathub
    - Fedora
    - KDE
    - GNOME Nightly if you activate that


3.  installing Flatpaks
    - you have to edit this script, remove the "#" to install the packages


4. Installing Snap Package manager
    - you have to manually activate that
    - allowing /home to be used through /var/home, this removes the containerization of Kionite in a way!


5. Configuring settings
    - enabling automatic rpm-ostree updates (you still need to reboot)
    - Automatic Flatpak updates via cron.daily (every day)
    - enabling Mac-Adress randomization for privacy
    - enabling 
    - TLP as systemd module for Battery saving
    - setting up a nice GRUB theme
    - applying UEFI Firmware updates
    - theme flatpaks using your set GTK theme


6. Downloading Microsoft Fonts for compatibility (Times, Arial, Cambria,...)


7. Downloading Lynis and making a security audit


8. Setting up RPMfusion repositories
    - deactivated by default, as you should install as little as possible
    - This includes the RPMFusion "free" and "nonfree" variant
    - a special RPMfusion repo is needed to play DVDs (VLC has that package included, other Flatpaks don't)

    - Added Repositories slow down rpm-ostree updates even more!
    

9. Installing RPM Packages
    - A lot is deactivated, try to get along without it, then use it
    - RPMs needed to deal with Windows stuff
    - RPMs not yet available as Flatpaks
    - MullvadVPN + setup (optional)


10. Installing the Android Emulator Waydroid
    - Adding the aleasto/waydroid repo
    
Part 2:
    - enabling TLP, fail2ban and more as systemd services
    
    - Downloading Android
    - configuring free form windows to use Android apps normally
    - NOT YET: configuring keyboard layout
    - not added: downloading and installing Android apps per ADB



Find Tips here: https://fedoramagazine.org/how-i-customize-fedora-silverblue-and-fedora-kinoite/

"""

echo """
#################################################################

1. Removing some unwanted Apps

Gwenview is kept, although XNView is better, as it can view JXL images

tmp2-abrmd resulted in crashes, thats why you may want it removed
(https://www.ifconfig.it/hugo/2020/01/linux-on-huawei-matebook-d/)
"""

# sudo rpm-ostree override remove kmag kmouse* #gwenview #tpm2-abrmd

echo """
#################################################################
Adding flathub repo, click "Install" when Discover opens
"""

flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

wget https://flathub.org/repo/flathub.flatpakrepo
xdg-open ~/flathub.flatpakrepo
wait 30
rm ~/flathub.flatpakrepo


echo """
#################################################################
Adding Fedora and KDE Flatpak repos
"""

flatpak remote-add --if-not-exists fedora oci+https://registry.fedoraproject.org

flatpak remote-add --if-not-exists kdeapps --from https://distribute.kde.org/kdeapps.flatpakrepo

#flatpak remote-add --if-not-exists gnome-nightly https://nightly.gnome.org/gnome-nightly.flatpakrepo

flatpak update --appstream && flatpak update


echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

Installing Flatpak apps
"""

flatpak install -y flathub com.github.tchx84.Flatseal;
flatpak install -y flathub com.xnview.XnViewMP;
flatpak install -y flatub org.keepassxc.KeePassXC

sudo rpm-ostree override remove firefox && exit && flatpak install -y flathub org.mozilla.firefox

xdg-settings set default-web-browser org.mozilla.firefox.desktop

#flatpak install -y flathub org.freefilesync.FreeFileSync;
#flatpak instal -y flathub com.github.zocker_160.SyncThingy
#flatpak install -y org.gnome.simplescan
#flatpak install -y org.kde.kate

# Messaging
#flatpak install -y flathub org.signal.Signal;
#flatpak install -y flathub org.telegram.desktop
#flatpak install -y flathub im.riot.Riot
#flatpak install -y flathub eu.betterbird.Betterbird

# Internet
#flatpak install -y flathub website.i2pd.i2pd;
#flatpak install -y flathub org.onionshare.OnionShare
#flatpak install -y flathub com.github.micahflee.torbrowser-launcher
#flatpak install -y flathub org.qbittorrent.qBittorrent
# flatpak install -y flathub com.github.gabutakut.gabutdm

# Media
#flatpak install -y flathub org.videolan.VLC
#flatpak install -y flathub bimp;
#flatpak install -y flathub dev.alextren.Spot;
#flatpak install -y flathub io.freetubeapp.FreeTube;
#flatpak install -y app.rafaelmardojai.Blanket;
#flatpak install -y flathub com.spotify.Client;
#flatpak install -y flathub com.github.wwmm.easyeffects
#flatpak install -y flathub com.xnview.XnConvert
#flatpak install -y flathub org.gimp.GIMP

#flatpak install -y flathub fr.handbrake.ghb fr.handbrake.ghb.Plugin.IntelMediaSDK
#flatpak install -y flathub com.obsproject.Studio
#flatpak install -y flathub com.obsproject.Studio.Plugin.OBSVkCapture #and other plugins


# Crypto
#flatpak install -y flathub monero-gui;
#flatpak install -y flathub org.cryptomator.Cryptomator;

# Wine
# flatpak install -y flathub org.winehq.Wine org.winehq.Wine.DLLs.dxvk org.winehq.Wine.gecko org.winehq.Wine.mono

echo "removing unused Flatpak Libraries (probably none)"
flatpak uninstall -y --unused


echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

Adding the Snapd app for installing Snaps

see: https://nelsonaloysio.medium.com/installing-ubuntus-snap-on-fedora-silverblue-e82ca6fd6108
"""

#sudo printf """[Unit]
Description=Enable mount points in / for OSTree
DefaultDependencies=no[Service]
Type=oneshot
ExecStartPre=chattr -i /
ExecStart=/bin/sh -c "[ -L '%f' ] && rm '%f'; mkdir -p '%f'"
ExecStopPost=chattr +i /""" > /etc/systemd/system/mkdir-rootfs@.service

#sudo printf """[Unit]
After=mkdir-rootfs@snap.service
Wants=mkdir-rootfs@snap.service
Before=snapd.socket[Mount]
What=/var/lib/snapd/snap
Where=/snap
Options=bind
Type=none[Install]
WantedBy=snapd.socket""" > /etc/systemd/system/snap.mount

#sudo printf """[Unit]
After=mkdir-rootfs@home.service
Wants=mkdir-rootfs@home.service
Before=snapd.socket[Mount]
What=/var/home
Where=/home
Options=bind
Type=none[Install]
WantedBy=snapd.socket""" > /etc/systemd/system/home.mount

#sudo cp /etc/passwd /etc/passwd.bak &&
#sudo sed -i 's:/var/home:/home:' /etc/passwd

#sudo systemctl daemon-reload &&
#sudo systemctl start {home.mount,snap.mount} &&
#sudo systemctl enable {home.mount,snap.mount}

#echo "installing Snapd..."
#sudo rpm-ostree install snapd
#sudo snap update


# ---------- Different method ------------
echo """
Or install it through Toolbox (less security impact but requires more resources)
"""

# toolbox create -y snap && toolbox enter snap && sudo dnf install -y snapd

echo """
##########################
find Snaps using snap find
install snaps using snap install
"""


echo """
#################################################################
Configuring Settings

Auto-Updates (rpm-ostree and Flatpak):
https://github.com/tonywalker1/silverblue-update
"""

git clone https://github.com/tonywalker1/silverblue-update.git ~/silverblue-update
cd silverblue-update/
sudo chmod +x install.sh
sudo sh install.sh

echo """
Removing Discover notification...
"""
sudo rm /etc/xdg/autostart/org.kde.discover.notifier.desktop

# --- rpm-ostree timer native way
#sudo sed -i 's/none/stage/g' /etc/rpm-ostreed.conf  #set to install if set to none
#sudo sed -i 's/check/stage/g' /etc/rpm-ostreed.conf #set to install if set to check
#rpm-ostree reload
#systemctl enable rpm-ostreed-automatic.timer --now

# ---- mac adresses

echo "enabling mac adress randomization for privacy"
sudo printf "[device-mac-randomization]\nwifi.scan-rand-mac-address=yes\n[connection-mac-randomization]\nethernet.cloned\nmac-address=random\nwifi.cloned-mac-address=random" > /etc/NetworkManager/conf.d/99-custom.conf

echo """ 
Setting TLP as energy saving service

What is better, power profiles or TLP?
- different opinions
- Power profiles is more agressive on CPU
- TLP is more agressive on external ports
- TLP is reported to increase battery life more
"""

echo "enabling TLP for saving battery"

sudo systemctl enable --now tlp.service
sudo systemctl mask power-profiles-daemon.service #overwrites system internal power management
sudo systemctl mask systemd-rfkill.socket #enable radion device switching
sudo systemctl mask systemd-rfkill.socket

echo "disabling Geoclue agent (localizaion, important but running in the background all the time)"

sudo systemctl disable geoclue

echo """#################################################################

Updating the firmware, if an update is available
"""
sudo fwupdmgr refresh; sudo fwupdmgr get-updates; sudo fwupdmgr update


# Grub-Theme
echo "Installing a fancy GRUB bootloader theme"
wget https://github.com/vinceliuice/grub2-themes.git
unzip grub2-themes*.zip
rm grub2-themes*.zip
cd ~/grub2-themes-master/
sudo chmod +x install.sh
sudo sh install.sh -t vimix -b

echo """
#################################################################
Searching for a Download manager for multithreaded Downloads?
"""

firefox https://addons.mozilla.org/en-US/firefox/addon/multithreaded-download-manager/

echo """
#################################################################
Installing Microsoft Fonts to ~/.local/share/fonts/mscorefonts
"""

mkdir -p ~/.local/share/fonts/mscorefonts

wget https://cloud.uol.de/s/6HtRPcJZeMip7aC -P ~/

cd ~/
unzip ms-corefonts.zip
rm ms-corefonts.zip

cp -v ms-corefonts/*.ttf ms-corefonts/*.TTF ~/.local/share/fonts/mscorefonts/

#echo "Enabling System wide, currently no Flatpak support:"
#sudo mkdir -p /usr/local/share/fonts/mscorefonts/
#sudo cp -v fonts/*.ttf fonts/*.TTF /usr/local/share/fonts/mscorefonts/

echo """#################################################################
Enabling Flatpaks to use the local GTK theme. The GTK theme can be set in KDE Settings and may adapt to the KDE (Qt) Theme.

https://itsfoss.com/flatpak-app-apply-theme/

reset with: sudo flatpak override --reset
"""

sudo flatpak override --filesystem=$HOME/.themes


echo """#################################################################
Running Lynis for security auditing

https://github.com/CISOfy/lynis

"""

git clone https://github.com/CISOfy/lynis && sudo ~/lynis/lynis audit system


# echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

Adding RPMfusion repos, please uncomment what you need

"rpmfusion-free-release-tainted" is needed for playing DVDs if the flatpak app requests it
"""

#sudo rpm-ostree --install rpmfusion-free-release-tainted #--install rpmfusion-free-release #--install rpmfusion-nonfree-release

#echo """
#################################################################
adding the BTFS COPR repository
"""
# sudo wget https://copr.fedorainfracloud.org/coprs/elxreno/btfs/repo/fedora-37/elxreno-btfs-fedora-37.repo -P /etc/yum.repos.d/

echo """
#################################################################

If you want to add a COPR repository, download its ".repo" file or do the ostree command:

sudo wget URL-TO-.repo-FILE -P /etc/yum.repos.d

sudo ostree remote add <name-of-repo> <repository-url>
"""



echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

Installing RPMs to layer over the Fedora base. Use layered RPMs as little as possible.


    If you just need a specific app not integrated into the system, try toolbox:

    toolbox create
    toolbox enter
    sudo dnf install APPNAME

#################################################################
"""

#echo """RPMs for Intel hardware video acceleration:"""

# rpm-ostree install intel-gpu-tools libva-intel-driver libva-intel-hybrid-driver libva-utils libva-vdpau-driver libvdpau-va-gl mpv vdpauinfo

#echo """Installing Media Codecs, for apps not integrating them
"""

#sudo rpm-ostree install -y gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel
#sudo rpm-ostree install -y lame\* --exclude=lame-devel
#rpm-ostree group upgrade --with-optional Multimedia


echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

Installing some needed RPMs:

Antivirus, Brute-Force Blocker, Battery-saver, Bittorrent filesystem, System cleaner, Video Thumbnails, Fingerprint sensor software, Python installer, ADB, Qemu emulator, OpenGL (for 3D-rendering)
"""

sudo rpm-ostree override remove libavcodec-free --install exiftool perl-Image-ExifTool clamtk* fail2ban tlp make gcc-c++ qemu-kvm qemu-img qemu-user-static kffmpegthumbnailer #libfprint unrar stacer pip android-tools btfs 



#sudo rpm-ostree install -y needrestart preload #only needed for RPMs ?
#sudo rpm-ostree install -y smem
#sudo rpm-ostree install -y libdvdcss* # maybe not needed, VLC Flatpak has it integrated, Handbrake doesnt is seems

# other packages you may want:
# sudo rpm-ostree install -y ffmpegthumbs btrbk ctags edk2-ovmf net-snmp postfix tmux-powerline waypipe flatpak-builder kernel-tools power-profiles-daemon pulseaudio-utils systemd-container ffmpeg-libs


# MullvadVPN
# xdg-open https://mullvad.net/download/app/rpm/latest/
# sudo rpm-ostree install ~/Downloads/mullvad*.rpm
# rm ~/Downloads/mullvad*.rpm


# echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

If you deal with Windows, these RPMs are useful, installing...

"""

#sudo rpm-ostree install -y woeusb* exfat-utils fuse-exfat

# echo """
#################################################################
If you have an Intel CPU, you may need these...
"""
#sudo rpm-ostree install intel-media-driver


# echo """
#################################################################

YOU NEED TO EDIT THIS SECTION

If you have an NVIDIA GPU, you need these, from the RPM-Fusion nonfree repo...

First determine what GPU you have

https://itsfoss.com/install-nvidia-drivers-fedora/

"""
lspci -vnn | grep VGA

xdg-open https://www.nvidia.com/Download/index.aspx?lang=en-us

#sudo rpm-ostree install akmod-nvidia xorg-x11-drv-nvidia-390xx akmod-nvidia-390xx xorg-x11-drv-nvidia-340xx akmod-nvidia-340xx

echo """
#################################################################

Installing Waydroid from the aleasto/waydroid COPR repository

(Currently there is no Flatpak for Waydroid, so it will be installed as overlay)

Using the Freeform Windows, you can start Waydroid Apps directly from your App menu!
"""

# other way, not sure if works
#sudo ostree remote add aleasto-waydroid-fedora-37.repo https://copr.fedorainfracloud.org/coprs/aleasto/waydroid/repo/fedora-37/aleasto-waydroid-fedora-37.repo

sudo wget https://copr.fedorainfracloud.org/coprs/aleasto/waydroid/repo/fedora-37/aleasto-waydroid-fedora-37.repo -P /etc/yum.repos.d/
sudo rpm-ostree install -y waydroid

reboot
