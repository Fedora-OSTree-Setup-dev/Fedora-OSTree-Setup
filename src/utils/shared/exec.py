from shutil import which
from subprocess import run, CalledProcessError, DEVNULL
from typing import NoReturn

from src.utils.log.logger import Logger


def execute_command(
        log: Logger, command: list[str], verbose: bool = False
    ) -> NoReturn | None:
    """For command execution/system calls with error handling

    Args:
        log -- Logger instance
        command -- command to execute with arguments

    Returns:
        None or raise system exit
    """

    try:
        if which(command[0]) is None:
            log.logger(
                "E", f"Program: {command[0]} does not exists, aborting ..."
            )
            raise SystemExit

        if verbose:
            return_code: int = run(command).returncode
        else:
            return_code: int = run(command, stdout=DEVNULL).returncode

        if return_code != 0:
            raise CalledProcessError(return_code, command)
        else:
            log.logger("I", f"Successfully executed the command: {command}")
    except (OSError, CalledProcessError) as Err:
        log.logger(
            "E",
            (
                f"{Err} encountered, cannot execute"
                " command: {command}, aborting ..."
            )
        )
        raise SystemExit

    return None
