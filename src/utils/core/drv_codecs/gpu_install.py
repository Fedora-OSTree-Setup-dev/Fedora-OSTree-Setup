from subprocess import CalledProcessError
from typing import Optional

from src.utils.shared.exec import exec_cmd
from src.utils.shared.log.logger import Logger


#! THIS IS EXPERIMENTAL AND NOT TESTED DUE TO LACK OF HARDWARE
#! SHOULD NOT BE CALLED YET ON THE MAIN FUNCTION IN MAIN.PY
#! ALTHOUGH THIS CAN BE ENABLED USING A FLAG `ex` IN THE CLI
#! BUT NOT IN DEFAULT OPTIONS, DO IT IN YOUR OWN DISCRETION

def fetch_gpu(log: Logger) -> Optional[list[list[str]]]:
    """Fetch the GPU of the system.

    Args:
        log -- instance of Logger

    Returns:
        The name of GPU or None.
    """

    try:
        gpu_name: Optional[str] = exec_cmd( # type: ignore
                log,
                ["grep", "-i", "VGA"],
                False,
                False,
                True,
                ["lspci"]
            )

    except (CalledProcessError, FileNotFoundError) as Err:
        log.logger("e", f"{Err}. Command lspci failed to execute.")
        return None
    else:
        return [
            gpu.split(":") for gpu in gpu_name.split(r"\n")
        ]


def install_gpu_drivers(log: Logger) -> list[str] | None:
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

        t_gpu_drv.append(gpu_drv.get(drv_id)) # type: ignore

    return t_gpu_drv
