from os import getenv
from typing import Optional

from rich.console import Console

from src.utils.shared.misc.uinput import uinput
from src.utils.shared.log.logger import Logger


def fetch_env(log: Logger, console: Console, env_var: str) -> str:
    """Fetch the value of given env variable.

    Args:
        log -- instance of Logger
        env_var -- variable to fetch

    Returns:
        The value of env variable
    """

    try:
        env_val: Optional[str] = getenv(env_var.upper())
    except OSError as Err:
        log.logger("e", f"{Err}. No value found for {env_var}.")
        env_val_u = uinput(
                console, f"Kindly input the value for {env_var}", 3
            )

    return env_val or env_val_u
