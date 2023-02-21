## How to use custom SDDM themes on Fedora Kinoite / OpenSuse microOS
Use a Distrobox or Toolbox container for this.

### 1. Install [sddm2rpm](https://github.com/Lunarequest/sddm2rpm)
```
sudo dnf install -y cargo
cargo add sddm2rpm
```
add "sddm2rpm" and all other cargo packages to your Path, making it directly executeable:
```
printf """
export PATH=/var/home/user/.cargo/bin/:$PATH""" >> ~/.bashrc
```

### 2. Download an SDDM theme you like
Go to [The KDE Store](https://store.kde.org/browse/) or [the Pling Store](https://www.pling.com/) and download and SDDM archive you like.

It has to be a .tar.* archive, not a .zip.

Open a Terminal in the download directory and run 

```
sddm2rpm name-of-theme.tar.gz
```

### Install the Theme
layer the rpm: Open the Terminal in the location of the new created RPM

```sudo rpm-ostree install theme.rpm

reboot```

(on openSuse microOS you would use `transactional-update install pkg theme.rpm`)

After rebooting go to the KDE settings, it will appear there.

### Change a theme
To change a themes background, just replace its "background.png" in the archive and repeat the rpm creation process.

Make sure to have all metadata, screenshots e.g. set right if you want to have a perfect experience.

You could just replace the background, but this would make it look wrong.
