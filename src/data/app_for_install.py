from dataclasses import dataclass


@dataclass
class GetApps:
    """Apps to be installed"""

    #* takes the name of the app, then a dictionary which includes the
    #* application id, and then a simple description for the given app
    recommend_list: dict[str, dict[str, str]] = {
            "Mailspring": {
                    "aid": "com.getmailspring.Mailspring",
                    "simple_description": "A simple email client."
                },
            "LibreOffice": {
                    "aid": "org.libreoffice.LibreOffice",
                    "simple_description": "Office suite."
                },
            "VLC": {
                    "aid": "org.videolan.VLC",
                    "simple_description": "Video player."
                },
            "Okular": {
                    "aid": "org.kde.okular",
                    "simple_description": "A document viewer."
                },
            "GIMP": {
                    "aid": "org.gimp.GIMP",
                    "simple_description": "Photo editing application."
                },
            "ClamTk": {
                    "aid": "com.gitlab.davem.ClamTk",
                    "simple_description": "Front end for ClamAV."
                },
            "FlatSeal": {
                    "aid": "com.github.tchx84.Flatseal",
                    "simple_description": (
                            "GUI for managing flatpak"
                            " applications permission"
                        )
                }
        }
    selected_app: list[str] = None
