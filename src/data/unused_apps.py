from dataclasses import dataclass


@dataclass(frozen=True)
class UnusedApps:
    """List of unused apps"""

    flatpaks_unused_apps: dict[str, str] = {
            "calculator": "org.gnome.Calculator",
            "calendar": "org.gnome.Calendar",
            "characters": "org.gnome.Characters",
            "connections": "org.gnome.Connections",
            "contacts": "org.gnome.Contacts",
            "Document Viewer": "org.gnome.Evince",
            "extensions": "org.gnome.Extensions",
            "logs": "org.gnome.Logs",
            "maps": "org.gnome.Maps",
            "text editor": "org.gnome.TextEditor",
            "weather": "org.gnome.Weather",
            "disk usage analyzer": "org.gnome.baobab",
            "clocks": "org.gnome.Clocks",
            "image viewer": "org.gnome.eog",
            "fonts": "org.gnome.fonts-viewer",
        }