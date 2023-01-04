from shutil import which
from subprocess import run, CalledProcessError, DEVNULL
from typing import NoReturn

from src.utils.shared.log.logger import Logger


def exec_cmd(
        log: Logger,
        command: list[str],
        verbose: bool = False,
        break_proc: bool = False
    ) -> NoReturn | None:
    """For command execution/system calls with error handling

    Args:
        log -- Logger instance
        command -- command to execute with arguments
        verbose -- whether to show command output or not
        break_proc -- whether to raise systemexit or not

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
            ret: int = run(command).returncode
        else:
            ret = run(command, stdout=DEVNULL).returncode

        if ret != 0:
            raise CalledProcessError(ret, command)
        else:
            log.logger("I", f"Successfully executed the command: {command}")
    except (OSError, CalledProcessError) as Err:
        log.logger(
            "E",
            (
                f"{Err} encountered, cannot execute"
                " command: {command} ..."
            )
        )

        if break_proc:
            raise SystemExit

    return None
