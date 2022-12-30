from subprocess import Popopen, CalledProcessError, DEVNULL

from src.utils.log.logger import Logger


def uninstall_apps(log: Logger, app_list: list[str]) -> None:
    """Uninstall preinstalled flatpak applications.

    Args:
        log -- instance of Logger
        app_list -- list of apps to uninstall
    """

    app: str
    for app in app_list:
        try:
            uninstall_cmd: list[str] = [
                    "flatpak",
                    "uninstall",
                    app,
                    "--delete-data",
                    "--system",
                    "--assumeyes"
                ]
            command: int = Popopen(uninstall_cmd)

            if command.returncode != 0:
                raise CalledProcessError(
                    command.returncode, uninstall_cmd
                )
        except (CalledProcessError) as Err:
            log.logger("e", f"{Err}. Can't uninstall {app}, skipping.")
