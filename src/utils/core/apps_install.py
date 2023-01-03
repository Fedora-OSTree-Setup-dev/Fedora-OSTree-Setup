from rich.console import Console

from src.utils.shared.exec import execute_command
from src.utils.shared.misc.uinput import uinput
from src.utils.shared.misc.title_banner import title_banner
from src.utils.shared.log.logger import Logger


class AppInstall:
    def __init__(
            self,
            log: Logger,
            console: Console,
            flatpak_list: dict[str, dict[str, str]],
            rpm_list: dict[str, dict[str, str]],
            verbose: bool = False
        ) -> None:
        """
        Args:
            log -- instance of Logger
            console -- instace of console
            flatpak_list -- lists of the recommended applications
                including their application id (aid) and description
            rpm_list -- lists of the recommended applications
                including their application id (aid) and description
            verbose -- whether to display the process output or not
        """

        self.log: Logger = log
        self.console: Console = console
        self.FLATPAK_APP_LIST: dict[str, dict[str, str]] = flatpak_list
        self.RPM_APP_LIST: dict[str, dict[str, str]] = rpm_list
        self.verbose: bool = verbose

        self.FLATPAK_APP_INDEX: dict[int, str] = {
                index: aid for index, aid in zip(
                    range(len(self.FLATPAK_APP_LIST.items())),
                    self.FLATPAK_APP_LIST.keys()
                )
            }
        self.RPM_APP_INDEX: dict[int, str] = {
                index: aid for index, aid in zip(
                    range(len(self.RPM_APP_LIST.items())),
                    self.RPM_APP_LIST.keys()
                )
            }

    def _enum_apps(
            self,
            app_index: dict[int, str],
            app_list: dict[str, dict[str, str]]
        ) -> None:
        """Enumerate the apps in the list and print out with a format.

        Args:
            app_index -- index of applications and their name
            app_list -- lists of the recommended applications including
                their application id (aid) and description
        """

        index: int; appname: str
        for index, appname in app_index.items():
            self.console.print(
                (
                    f"[bold cyan]{index:4}[/bold cyan] "
                    f"[bold]{appname}[/bold] -- "
                    f"{app_list.get(appname).get('sdesc')}" # type: ignore
                )
            )

        return None

    def app_install(self) -> None:
        """For installation of recommended program selected by user."""


        for apptype, applist in {
                "flatpak": {
                        "index": self.FLATPAK_APP_INDEX,
                        "list": self.FLATPAK_APP_LIST
                    },
                "rpm": {
                        "index": self.RPM_APP_INDEX,
                        "list": self.RPM_APP_LIST
                    }
            }.items():
            title_banner(
                "installation of recommended apps",
                f"recommended apps ({apptype})"
            )
            self._enum_apps(
                applist.get("index"), applist.get("list")
            )

        selected_app: list[int] = uinput(
                self.console,
                "Input the number of applications to install",
                2
            )

        aindex: int
        for aindex in selected_app:
            sapp_id: str = self.FLATPAK_APP_LIST.get( # type: ignore
                    self.FLATPAK_APP_INDEX.get(aindex)).get("aid" # type: ignore
                )
            install_cmd: list[str] = [
                    "flatpak",
                    "install",
                    "flatpak",
                    sapp_id
                ]
            execute_command(self.log, install_cmd, self.verbose)

        return None
