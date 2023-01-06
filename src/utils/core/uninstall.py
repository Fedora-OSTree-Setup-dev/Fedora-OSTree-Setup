from src.utils.shared.misc.section import section
from src.misc.alias import ProgData


class Uninstall:
    """For uninstallation of programs."""

    def __init__(
            fp_data_arr: ProgData, rpm_data_arr: ProgData
        ) -> None:
        pass

    def uninstall_apps(
            prog_arr: list[str], progtype: str
        ) -> list[list[str]] | list[str]:
        """Uninstall preinstalled flatpak applications.

        Args:
            prog_arr -- list of apps to uninstall
            progtype -- the type of application to remove

        Returns:
            An array of the appropriate uninstall commands or array of the
            applications to uninstall
        """

        t_fp_cmd: list[list[str]] = []

        prog: str
        for prog in prog_arr:
            section(
                "uninstallation of unnecessary preinstalled programs",
                f"listed unnecessary preinstalled programs ({progtype})"
            )
            uninstall_cmd: list[str] = [
                    "flatpak",
                    "uninstall",
                    prog,
                    "--delete-data",
                    "--system",
                    "--assumeyes"
                ]
            t_fp_cmd.append(uninstall_cmd)

        return t_fp_cmd
