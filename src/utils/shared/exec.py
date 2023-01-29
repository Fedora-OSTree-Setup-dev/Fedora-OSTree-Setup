from shutil import which
from subprocess import run, CalledProcessError, DEVNULL, Popen, PIPE, check_output
from typing import NoReturn, Optional

from src.utils.shared.log.logger import Logger


def exec_cmd(
        log: Logger,
        cmd: list[str],
        verbose: bool = False,
        break_proc: bool = False,
        pipe_: bool = False,
        init_cmd: Optional[list[str]] = None
    ) -> NoReturn | None:
    """For command execution/system calls with error handling

    Args:
        log -- Logger instance
        cmd -- command to execute with arguments
        verbose -- whether to show command output or not
        break_proc -- whether to raise systemexit or not
        pipe_ -- whether to pipe a command or not
        init_cmd -- initial command to be piped to the main command

    Returns:
        None, the output of the command or raise system exit
    """

    try:
        if which(cmd[0]) is None:
            log.logger(
                "E", f"Program: {cmd[0]} does not exists, aborting ..."
            )
            raise SystemExit

        if pipe_:
            init_cmd_out = Popen(init_cmd, stdout=PIPE)
            pipe_cmd: bytes = check_output(
                cmd, stdin=init_cmd_out.stdout
            )
            init_cmd_out.wait()

            if init_cmd_out.returncode != 0:
                CalledProcessError(init_cmd_out.returncode, init_cmd)

            return pipe_cmd.decode("utf-8").strip().replace(r"\n", "")
        
        if verbose:
            ret: int = run(cmd).returncode
        else:
            ret = run(cmd, stdout=DEVNULL).returncode

        if ret != 0:
            raise CalledProcessError(ret, cmd)

        log.logger("I", f"Successfully executed the command: {cmd}")
    except (OSError, CalledProcessError) as Err:
        log.logger(
            "E",
            (
                f"{Err} encountered, cannot execute"
                " command: {cmd} ..."
            )
        )

        if break_proc:
            raise SystemExit

    return None
