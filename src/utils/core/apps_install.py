from src.utils.shared.exec import execute_command
from src.utils.shared.uinput import uinput
from src.utils.shared.log.logger import Logger


def app_install(
        log: Logger, app_for_install: dict[str, dict[str, str]]
    ) -> None:
    """For installation of recommended applications selected by the user.

    Args:
        log -- instance of Logger
        app_for_install -- lists of the recommended applications including
            their application id (aid) and description
    """

    pass
