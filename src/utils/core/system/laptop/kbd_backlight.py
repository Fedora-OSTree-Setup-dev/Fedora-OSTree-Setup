from glob import glob
from os.path import isfile
from typing import Optional, NoReturn

from rich.console import Console

from src.utils.shared.exec import exec_cmd
from src.utils.shared.misc.uinput import uinput
from src.utils.shared.log.logger import Logger


def kbd_backlit_support_check(log: Logger) -> str | None:
    """Check if the device has a keyboard backlight.

    Returns:
        A boolean value corresponding to whether the kbd backlight works
    """

    try:
        file: str
        for file in glob("/sys/class/leds"):
            if isfile(file) and file.endswith("::kbd_backlight"):
                return file
    except (PermissionError, OSError, FileNotFoundError) as Err:
        log.logger(
            "E",
            (
                f"{Err}. Cannot determine whether"
                " the device supports backlight."
            )
        )

    return None


def check_kbd_backlit(log: Logger, console: Console) -> bool | NoReturn:
    """Check whether the kbd backlit works by default keybinding,
    if not install brightnessctl and bind to a specific command."""

    fname: Optional[str]; i: int
    if fname := kbd_backlit_support_check(log):
        for i in range(1, 4):
            exec_cmd(
                log,
                [
                    "sudo",
                    "tee",
                    "-a",
                    f"/sys/class/leds/{fname}"
                ],
                False,
                False,
                True,
                [
                    "echo",
                    i
                ]
            )

            if uinput(console, "Does the keyboard backlight work?", 1):
                return True

    return False
