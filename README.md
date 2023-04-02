# Fedora-OSTree-Setup
A small program making the install of Fedora Silverblue / Kionite easy. It lets you choose what to install or set.
![Fedora CoreOS Logo](https://avatars.githubusercontent.com/u/3730757?s=200&v=4)

## Why this is needed
An OSTree-based Fedora system can result in a pretty perfect and unbreakable experience.
- Your system stays pretty much the same as the developers version. This makes bugfixes and support easier.
- You install external Apps as Flatpaks or through Podman containers. You can use any Flatpak, Ubuntu, Fedora, Arch e.g. apps you want, but they can't break your system
- The system can update automatically, if an update breaks something, you can reboot and use the older version.

But Fedora Kinoite/Silverblue (and possibly versions with other Desktops like XFCE) are not really well setup out of the box. 
- no automatic updates for System and Flatpaks, system updates take very long though
- Native Firefox installed but it can't play Videos
- adding COPR repositories or other external ones is complicated
- changing the SDDM theme is not possible, but the standard theme looks very outdated
- Energy settings, Graphic drivers etc. are not preinstalled automatically (detecting hardware)
- There are too many packages preinstalled for the taste of some users
- There are cursos Issues in Flatpak applications
- The Android emulator Waydroid is very complicated to install
- The standard shell "bash" is behind "fish" in user experience
- ...

**We aim to fix all of these issues with this project!**

When it is finished, there will be instructions on how to install it. It will be user-interactive, leaving control for the user.
