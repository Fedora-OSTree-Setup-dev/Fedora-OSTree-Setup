from typing import Any

from rich.console import Console
from psutil import disk_partitions
from blkinfo import BlkDiskInfo # type: ignore

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

        def check_if_ssd() -> bool: # type: ignore
            """Check if the system is installed on ssd or not.

            Returns
                A boolean value pertaining to whether it is or not.
            """

            ...

        def check_if_encrypted() -> str | bool: # type: ignore
            """Check if the devices are encrypted or not.

            Returns
                if the device is encrypted, return the name of the
                    device,
                if otherwise, return false.
            """

            dev_name: str = [
                    dev.device for dev in disk_partitions()
                    if (
                            dev.device.startswith("/dev/mapper")
                            and dev.mountpoint.strip() == "/"
                        )
                ][0] #* get the first encrypted device mounted in /

            # if not dev_info :
            #     return False

            # dev_info: BlkDiskInfo = BlkDiskInfo().get_disks(
            #         {
            #             "name":
            #         }
            #     )


