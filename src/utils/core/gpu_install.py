from subprocess import (
    Popen,
    CalledProcessError,
    PIPE,
    check_output
)
from typing import Optional

from src.utils.shared.log.logger import Logger


def fetch_gpu(log: Logger) -> Optional[list[list[str]]]:
    """Fetch the GPU of the system.

    Args:
        log -- instance of Logger

    Returns:
        The name of GPU or None.
    """

    try:
        lspci_out = Popen(["lspci"], stdout=PIPE)
        gpu_name: bytes = check_output(
                ["grep", "-i", "VGA"], stdin=lspci_out.stdout
            )
        lspci_out.wait()

        if lspci_out.returncode != 0:
            raise SystemExit(["lspci"], lspci_out.returncode)
    except (CalledProcessError, FileNotFoundError) as Err:
        log.logger("e", f"{Err}. Command lspci failed to execute.")
        return None
    else:
        return [
            gpu.split(":") for gpu in (
                gpu_name
                    .decode("utf-8")
                    .strip()
                    .split("\n")
            )
        ]


def install_gpu_drivers(log: Logger) -> list[str]:
    """Append the appropriate driver in the list for GPU installation.

    Args:
        log -- instance of Logger

    Returns:
        true if the GPU was installed successfully or a temporary list
        for the appropriate gpu drivers
    """

    #! THIS IS EXPERIMENTAL AND NOT TESTED DUE TO LACK OF HARDWARE
    #! SHOULD NOT BE CALLED YET ON THE MAIN FUNCTION IN MAIN.PY
    #! ALTHOUGH THIS CAN BE ENABLED USING A FLAG `ex` IN THE CLI
    #! BUT NOT IN DEFAULT OPTIONS, DO IT IN YOUR OWN DISCRETION

    gpu_arr: Optional[list[list[str]]] = fetch_gpu(log)

    t_gpu_drv: list[str] = []

    if not gpu_arr:
        log.logger(
            "I", "There is no GPU driver to install, skipping ..."
        )
        return None

    gpu_drv: dict[str | list[str], list[str]] = {
            "nvidia": ["akmod-nvidia", "xorg-x11-drv-nvidia"],
        }

    gpu: list[str]
    for gpu in gpu_arr:
        vendor: str; gpu_info: list[str]
        vendor, *gpu_info = gpu

        match [vendor, *gpu_info]:
            case ["nvidia", *gpu_info]:
                drv_id: str = "nvidia"
            case ["intel", *gpu_info]:
                ...
            case ["advanced micro devices", *gpu_info]:
                ...

        t_gpu_drv.append(gpu_drv[drv_id])

    return t_gpu_drv
