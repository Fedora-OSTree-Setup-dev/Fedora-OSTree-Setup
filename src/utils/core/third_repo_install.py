from rich.console import Console

from src.utils.misc.uinput import uinput
from src.utils.log.logger import Logger


def third_repo_install(
        log: Logger, console: Console, commands: list[str]
    ) -> None:
    """Install third party repositories."""

    tp_repo: dict[int, dict[str, str]] = {
            # id and name of the repo and the address
            1: {
                    "name": "RPMFusion (Free)",
                    "desc": "Fedora repository for open source softwares.",
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"free/fedora/rpmfusion-free-release"
                            r"-$(rpm -E %fedora).noarch.rpm"
                        )
                },
            2: {
                    "name": "RPMFusion (Non-free)",
                    "desc": "Fedora repository for propietary software.",
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"nonfree/fedora/rpmfusion-nonfree"
                            r"-release-$(rpm -E %fedora).noarch.rpm"
                        )
                },
            3: {
                    "name": "Flathub",
                    "desc": "Unfiltered repository for flatpaks.",
                    "address": "https://flathub.org/repo/flathub.flatpakrepo"
                }
        }

    for info in tp_repo.values():
        if uinput(
                console, f"Install {info.get('name')} ({info.get('desc')})", 1
            ):
            commands.append()
