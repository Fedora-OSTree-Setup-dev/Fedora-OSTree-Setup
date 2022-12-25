from dataclasses import dataclass


@dataclass
class GetApps:
    """Apps to be installed"""

    recommend_list: dict[str, dict[str, str]] = {
            "mailspring": {
                    "aid": "com.getmailspring.Mailspring",
                    "simple_description": "A simple email client."
                },
            "libreoffice": {
                    "aid": "org.libreoffice.LibreOffice",
                    "simple_description": "Office suite."
                },
            "vlc": {
                    "aid": "org.videolan.VLC",
                    "simple_description": "Video player."
                },
            "okular": {
                    "aid": "org.kde.okular",
                    "simple_description": "A document viewer."
                },
            "gimp": {
                    "aid": "org.gimp.GIMP",
                    "simple_description": "Photo editing application."
                }
        }
    selected_app: list[str] = None
