from typing import Any

from rich.console import Console

from src.utils.shared.exec import execute_command
from src.utils.shared.misc.uinput import uinput
from src.utils.shared.misc.title_banner import title_banner
from src.utils.shared.log.logger import Logger
from src.misc.alias import AppData, AppIndex



class AppInstall:
    def __init__(
            self,
            log: Logger,
            console: Console,
            flatpak_list: AppData,
            rpm_list: AppData,
            flatpak_cmd_list: list[str],
            rpm_install_list: list[str],
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
            rpm_install_list -- list where the rpm that will be install
                is contained
            verbose -- whether to display the process output or not
        """

        self.log: Logger = log
        self.console: Console = console
        self.FLATPAK_APP_LIST: AppData = flatpak_list
        self.RPM_APP_LIST: AppData = rpm_list
        self.rpm_to_install: list[str] = rpm_install_list
        self.flatpak_cmd_list: list[str] = flatpak_cmd_list
        self.verbose: bool = verbose

        self.FLATPAK_APP_INDEX: AppIndex = {
                index: aid for index, aid in zip(
                    range(len(self.FLATPAK_APP_LIST.items())),
                    self.FLATPAK_APP_LIST.keys()
                )
            }
        self.RPM_APP_INDEX: AppIndex = {
                index: aid for index, aid in zip(
                    range(len(self.RPM_APP_LIST.items())),
                    self.RPM_APP_LIST.keys()
                )
            }

    def _enum_apps(
            self,
            app_index: AppIndex,
            app_list: AppData,
            apptype: str
        ) -> Any:
        """Enumerate the apps in the list and print out with a format.

        Args:
            app_index -- index of applications and their name
            app_list -- lists of the recommended applications including
                their application id (aid) and description
            apptype -- type of application, where flatpak or rpm
        """

        title_banner(
            "installation of recommended apps",
            f"recommended apps ({apptype})"
        )

        index: int; appname: str
        for index, appname in app_index.items():
            self.console.print(
                (
                    f"[bold cyan]{index:4}[/bold cyan] "
                    f"[bold]{appname}[/bold] -- "
                    f"{app_list.get(appname).get('sdesc')}" # type: ignore
                )
            )

        return uinput(
            self.console,
            "Input the number of applications to install",
            2
        )

    def app_install(self) -> tuple[list[str], list[str]]:
        """For installation of recommended program selected by user."""

        # fappsindex -> flatpak apps index
        # rappsindex -> rpm apps index
        fappsindex: int; rappindex: int

        #* FOR FLATPAK PROGRAMS
        #* appends the flatpak commands that needs to be executed in
        #* flatpak_cmd_list for a single execution of commands
        for fappsindex in self._enum_apps(
                self.FLATPAK_APP_INDEX, self.FLATPAK_APP_LIST, "flatpak"
            ):
            fapp_id: str = self.FLATPAK_APP_LIST.get(
                    self.FLATPAK_APP_INDEX.get(fappsindex) # type: ignore
                ).get("aid")
            install_cmd: list[str] = [
                    "flatpak",
                    "install",
                    "flathub",
                    fapp_id,
                    "--assumeyes"
                ]

            self.flatpak_cmd_list.append(install_cmd)

        #* FOR RPM PROGRAM
        #* appends the list of name of the selected rpm applications
        for rappindex in self._enum_apps(
                self.RPM_APP_INDEX, self.RPM_APP_LIST, "rpm"
            ):
            rapp_id: str = self.RPM_APP_LIST.get( # type: ignore
                    self.RPM_APP_INDEX.get(rappindex) # type: ignore
                ).get("aid")
            self.rpm_to_install.append(rapp_id)

        return self.rpm_to_install
