from rich.console import Console

from src.utils.shared.exec import exec_cmd
from src.utils.shared.misc.uinput import uinput
from src.utils.shared.log.logger import Logger


class SysOpt:
    """For system optimizations"""

    def disable_services(
            console: Console, log: Logger, verbose: bool = False
        ) -> None:
        """Disable autostart/systemd services that is not necessary

        Args:
            console -- instance of console
            log -- instance of logger
            verbose -- whether to show the stdout of cmds
        """

        cmd_arr: list[list[str]] = [
                [
                    "sudo",
                    "systemctl",
                    "disable",
                    "NetworkManager-wait-online.service"
                ],
                [
                    "sudo",
                    "rm",
                    "/etc/xdg/autostart/org.gnome.Software.desktop"
                ]
            ]

        cmd: str
        for cmd in cmd_arr:
            if uinput(console, f"Execute: {cmd}", 1):
                exec_cmd(log, cmd, verbose)
