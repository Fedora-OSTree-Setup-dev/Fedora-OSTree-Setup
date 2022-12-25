from subprocess import (
    Popen,
    CalledProcessError,
    PIPE,
    check_output
)

from src.utils.log.logger import Logger


def fetch_gpu(log: Logger) -> tuple[str, str | None] | None:
    """Fetch the GPU of the system.

    Args:
        log -- instance of Logger

    Returns:
        The name of GPU or None.
    """

    try:
        lspci_out = Popen(("lspci"), stdout=PIPE)
        gpu_name: str = check_output(
                ["grep", "-i", "VGA"], stdin=lspci_out.stdout
            )
        lspci_out.wait()

        if lspci_out.returncode != 0:
            raise SystemExit(["lspci"], lspci_out.returncode)
    except (CalledProcessError, FileNotFoundError) as Err:
        log.logger("e", f"{Err}. Command lspci failed to execute.")
        return None
    else:
        return gpu_name.decode("utf-8").strip().split("\n")
