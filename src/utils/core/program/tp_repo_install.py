from rich.console import Console

from src.utils.shared.misc.uinput import uinput


def tp_repo_install(
        console: Console
    ) -> tuple[list[list[str]], list[str]]:
    """Install third party repositories.

    Args:
        log -- instance of Logger
        console -- instance of Console
    """

    tp_repo: dict[int, dict[str, str]] = {
            # id and name of the repo and the address
            1: {
                    "name": "rpm_RPMFusion Free",
                    "id": "rpm_rfusion_f",
                    "desc": (
                            "Software that uses a free "
                            "license, but is not accepted "
                            "in Fedora for various reasons."
                        ),
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"free/fedora/rpmfusion-free-release"
                            r"-$(rpm -E %fedora).noarch.rpm"
                        )
                },
            2: {
                    "name": "rpm_RPMFusion Non-free",
                    "id": "rpm_rfusion_nf",
                    "desc": (
                            "Software that uses a nonfree "
                            "license, but is otherwise redistributable."
                        ),
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"nonfree/fedora/rpmfusion-nonfree"
                            r"-release-$(rpm -E %fedora).noarch.rpm"
                        )
                },
                        7: {
                    "name": "RPMFusion Free (Tainted)",
                    "id": "rpm_rfusion_f_tainted",
                    "desc": (
                            "Software that use a free license, but may"
                            " have usage restriction in some countries"
                        ),
                    "address": "rpmfusion-free-release-tainted"
                },
            3: {
                    "name": "RPMFusion Non-free (Tainted)",
                    "id": "rpm_rfusion_nf_tainted",
                    "desc": (
                            "Software that uses a nonfree license and "
                            "which is not explicitly redistributable, "
                            "but is allowed for inter-operability "
                            "purposes in some countries."
                        ),
                    "address": "rpmfusion-nonfree-release-tainted"
                },
            4: {
                    "name": "fp_Flathub",
                    "id": "fp_flathub",
                    "desc": "Unfiltered repository for flatpaks.",
                    "address": (
                            "https://flathub.org/repo"
                            "/flathub.flatpakrepo"
                        )
                },
            5: {
                    "name": "Fedora OCI (Flatpak)",
                    "id": "fp_fed_oci",
                    "desc": "For Open Containers Initiative (OCI)", #? what's this for?
                    "address": "oci+https://registry.fedoraproject.org"
                },
            6: {
                    "name": "KDE (Flatpak)",
                    "id": "fp_kde",
                    "desc": "KDE Applications.",
                    "address": (
                            "https://distribute.kde.org/"
                            "skdeapps.flatpakrepo"
                        )
                },
            7: {
                    "name": "GNOME Nightly (Flatpak)",
                    "id": "fp_gnome_nightly",
                    "desc": "For cutting edge builds from GNOME.",
                    "address": (
                            "https://nightly.gnome.org/"
                            "gnome-nightly.flatpakrepo"
                        )
                },
        }

    t_fp_cmd: list[list[str]] = []
    t_rfusion: list[str] = []

    for repo in tp_repo.values():
        if uinput(
                console,
                f"Install {repo.get('name')} ({repo.get('desc')})",
                1
            ):
            repo_id: str = repo.get("id") # type: ignore
            if repo_id.startswith("fp_"):
                t_fp_cmd.append(
                    [
                        "flatpak",
                        "remote-add",
                        "--if-not-exists",
                        repo.get("name"), # type: ignore
                        repo.get("address") # type: ignore
                    ]
                )
                continue

            t_rfusion.append(repo.get("address")) # type: ignore

    return t_fp_cmd, t_rfusion
