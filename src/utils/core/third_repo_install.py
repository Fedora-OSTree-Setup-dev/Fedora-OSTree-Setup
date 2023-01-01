from typing import Any

from rich.console import Console

from src.utils.shared.uinput import uinput


def third_repo_install(
        console: Console,
        commands: list[str],
        rpmfusion_repo: list[Any]
    ) -> None:
    """Install third party repositories.

    Args:
        log -- instance of Logger
        console -- instance of Console
        commands -- list of commands for execution
        rpmfusion_repo -- list of packages to be installed
    """

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

    for repo in tp_repo.values():
        if uinput(
                console, f"Install {repo.get('name')} ({repo.get('desc')})", 1
            ):
            if repo.get("name") == "flathub":
                commands.append(
                    (
                        "flatpak remote-add --if-not-exists flathub "
                        "https://flathub.org/repo/flathub.flatpakrepo"
                    )
                )
                continue
            rpmfusion_repo.append(repo.get("address"))

    return None
