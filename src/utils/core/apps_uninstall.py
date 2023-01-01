from src.utils.shared.exec import execute_command
from src.utils.shared.log.logger import Logger


def uninstall_apps(
        log: Logger,
        app_list: list[str],
        verbose: bool = False,
    ) -> None:
    """Uninstall preinstalled flatpak applications.

    Args:
        log -- instance of Logger
        app_list -- list of apps to uninstall
        verbose -- whether to show command output or not
    """

    app: str
    for app in app_list:
        uninstall_cmd: list[str] = [
                "flatpak",
                "uninstall",
                app,
                "--delete-data",
                "--system",
                "--assumeyes"
            ]
        execute_command(log, uninstall_cmd, verbose)

    return None
