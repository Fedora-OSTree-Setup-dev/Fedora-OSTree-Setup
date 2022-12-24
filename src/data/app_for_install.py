from dataclasses import dataclass


@dataclass
class GetApps:
    """Apps to be installed"""

    recommend_list: dict[str, str] = {
            "mailspring": "com.getmailspring.Mailspring",
            "libreoffice": "org.libreoffice.LibreOffice",
            "vlc": "org.videolan.VLC",
            "okular": "org.kde.okular",
            "gimp": "org.gimp.GIMP"
        }
    selected_app: list[str] = None
