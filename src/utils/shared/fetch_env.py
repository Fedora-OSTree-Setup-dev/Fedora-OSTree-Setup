from os import getenv

from rich.console import Console

from src.utils.misc.uinput import uinput
from src.utils.log.logger import Logger


def fetch_env(log: Logger, console: Console, env_var: str) -> str:
    """Fetch the value of given env variable.

    Args:
        log -- instance of Logger
        env_var -- variable to fetch

    Returns:
        The value of env variable or None
    """

    try:
        env_value: str = getenv(env_var.upper())
    except OSError as Err:
        log.logger("e", f"{Err}. No value found for {env_var}.")
        env_value = uinput(
                console, f"Kindly input the value for {env_var}"
            )

    return env_value
