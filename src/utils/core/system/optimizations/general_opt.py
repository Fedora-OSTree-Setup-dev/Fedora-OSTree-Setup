from typing import Any

from rich.console import Console
from psutil import disk_partitions

from src.utils.shared.exec import exec_cmd
from src.utils.shared.fetch_env import fetch_env
from src.utils.shared.misc.uinput import uinput
from src.utils.shared.log.logger import Logger


class SysOpt:
    """For system optimizations"""

    def __init__(
            self, log: Logger, console: Console, verbose: bool = False
        ) -> None:
        """
        Args:
            log -- instance of logger
            console -- instance of console
            verbose -- whether to show the stdout of cmds
        """

        self.log: Logger = log
        self.console: Console = console

        self.verbose: bool = verbose

    def disable_services(self) -> None:
        """Disable autostart/systemd services that is not necessary"""

        cmd_arr: list[list[str]] = [
                [
                    "sudo",
                    "systemctl",
                    "disable",
                    "NetworkManager-wait-online.service"
                ],
            ]

        cmd: str | list[str]
        for cmd in cmd_arr:
            if uinput(self.console, f"Execute: {cmd}", 1):
                exec_cmd(self.log, cmd, self.verbose)

    def disable_workqueue(self) -> None:
        """Disable workqueue to improve ssd performance"""

        disk_names: list[str] = [
                parts.device for parts in disk_partitions()
            ]

        for disks in disk_names: ...

