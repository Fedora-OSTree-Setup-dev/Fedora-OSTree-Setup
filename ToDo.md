# To Do

## 1. GPU driver installation ([#5](/../../issues/5))

Intel:
- some drivers missing?

Nvidia:
- akmod-nvidia xorg-x11-drv-nvidia
- OR akmod-nvodia xorg-x11-drv-nvidia-cuda (for CUDA gpus)

## 2. DE based optimizations ([#11](/../../issues/11))

### Gnome (Silverblue)

- remove gnome software from autostart

### KDE (Kinoite)

- disable the annoying plopping sound
- ask to uninstall `kmousetool`, `kmag`, `Gwenview` (its kinda useless but easy to use and currently the only app supporting .jxl files)

## 3. Setup third party repo ([#6](/../../issues/6))

### flatpak (flathub)

- remove Fedora flatpak
- add flathub repo
- ask whether to install KDE and Gnome nightly repos

### RPMFusion

- nonfree
- free
- rpmfusion-nonfree-tainted for `libdvdcss2`

## 4. Install recommended flatpak apps ([#7](/../../issues/7))

- Security stuff like ClamAV and Flatseal should be installed nonetheless, maybe one question `do you use the Terminal for Flatpak and Antivirus tasks? y/n`

## 5. Configure Snap

- "WARNING: This shoud work, but is still experimental"
- Personally I found no app that I needed only on Snap
- Maybe we need a startup script that mount-binds /var/home to /home to prevent breakages
- at the end a short explanation about installing snaps
- does it automatically add the repo to Discover / GNOME Software?

## 6. Configure settings

- Automatic rpm-ostree and Flatpak updates through integration of [this nice script](https://github.com/tonywalker1/silverblue-update)
- enabling Mac-Adress randomization for privacy
- setting up a nice GRUB theme with asking, external github repo cloned
- applying UEFI Firmware updates using a systemd timer ([Fedora Silverblue autoupdates](https://github.com/tonywalker1/silverblue-update) as example of a really nice integration)
- theme flatpaks using your set GTK theme
- battery charging limit with asking
- disable Gnome software and Discover updates and background processes without asking, not needed anymore. Only useful for searching programs in the nice gui.
- my laptop always has too high mic volume, so I set it to 40% with a start script, yes/no and volume asked. This is added to the postinstall script, so it can be repeated when sure what volume is wanted. Message "you can replace the mic-value in the postinstall.sh script you find in the "bin" folder."
- grub menu has to be shown with 5 seconds to decide. Maybe the timespan can be asked, but if the system crashes, it has to be beginner-friendly to switch back to a previous tree

## 7. Hibernation:

- This is a big thing, very important, I asked already on ask fedora.
- Have to test, if a slight modification of [this solution](https://fedoramagazine.org/hibernation-in-fedora-36-workstation/) works

## 8. Downloading MS Fonts

- this is of course optional
- still not working in my script
- needs to support at least flatpak apps
- ask if also install for rpm apps (different folder, probably not needed)

## 9. Downloading Lynis

- `mkdir ~/bin` (there is a wget option to auto-create missing folders!)
- wget https://github.com/CISOfy/lynis/raw/master/lynis -P ~/bin/
- a systemd timer once a week, running only that command. Way better than cloning the whole repo

## 10. Installing `rpm-packages`

- NOTIFICATION: "You can do other stuff now, installing takes a while...", best as notification in the tray?
- `zenity --info --text="Installing packages...\n\nYou can do other stuff now\." --title="Info\!"`

- iaacornus: to me it seems better in notification tray?

- Speed: use extra script that is generated using appending the names
- As if want to game and use the custom RPM Proton https://github.com/GloriousEggroll/proton-ge-custom or the flatpak one without patches
- rpm-ostree override remove libavcodec-free --install exiftool perl-Image-ExifTool clamtk* fail2ban tlp make gcc-c++ qemu-kvm qemu-img qemu-user-static ffmpegthumbs kffmpegthumbnailer #libfprint unrar stacer pip android-tools btfs
- optional: install java, perl, not preinstalled

`printf "appnamex " >> ~/Fedora-OSTree-setup/rpm-install.sh`

at the end of all rpm-package y/n choices, the installscript is executed with sudo

### 10.1 Waydroid

- custom COPR repo! Display a small warning about that
- Only works on Wayland! But wayland is still buggy, display that as a message
- includes a few more steps, I got most of them ready
- all the settings in the post-reboot script are only triggered if you choose "yes"

`sed -i `s/#settingname //g` ~/bin/postinstall.sh`

## 11. Keyboard

- Layout chooseable after I found a solution where to get the .kml files from
- big if elif loop, with 1= en-Qwerty (no changes), 2 = QWERTZ, 3 = ...

## 12. Folder-Sync

- mount binded folders like Downloads, Pictures and Documents
- take the language from the keyboard language? question if this should be done
- manual: input of user "how is your Pictures folder called?", use that in mount-bind command

## 13. reboot settings

- the after-install script should be set as autostart script
- the rpm-ostree processes took a while, display a window saying "you can reboot your pc now", as a popup window. With a `wait 30` command a reboot is initiated automatically

## 14. Second script after reboot

- inits automatically, but in background! can this be changed?
- Waydroid settings
- RPM app settings?
- set systemd activities (tlp, clamtk, maybe Mullvad if installed)
- what else?
- at the end it has to be removed from startup scripts
