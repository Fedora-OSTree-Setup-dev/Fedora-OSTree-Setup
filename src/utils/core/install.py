from typing import Any

from src.utils.shared.misc.uinput import uinput
from src.utils.shared.misc.section import section
from src.misc.alias import ProgData, ProgIndex



class Install:
    """For installation of the recommended programs."""

    def __init__(
            self, fdata_arr: ProgData, rdata_arr: ProgData
        ) -> None:
        """
        Args:
            log -- instance of Logger
            fdata_arr -- lists of the recommended applications
                including their application id (aid) and description
            rdata_arr -- lists of the recommended applications
                including their application id (aid) and description
        """

        self.FPROG_ARR: ProgData = fdata_arr
        self.RPROG_ARR: ProgData = rdata_arr

        self.FPROG_INDEX: ProgIndex = { # index: program id of flatpak applications
                index: aid for index, aid in zip(
                    range(len(self.FPROG_ARR.items())),
                    self.FPROG_ARR.keys()
                )
            }
        self.RPROG_INDEX: ProgIndex = { # index: program id of flatpak applications
                index: aid for index, aid in zip(
                    range(len(self.RPROG_ARR.items())),
                    self.RPROG_ARR.keys()
                )
            }

    def _enum_prog(
            self,
            progindex: ProgIndex,
            progdata: ProgData,
            progtype: str
        ) -> Any:
        """Enumerate the programs in the list and print out with a format.

        Args:
            progindex -- index of applications and their name
            progdata -- lists of the recommended applications including
                their application id (aid) and description
            progtype -- type of application, where flatpak or rpm
        """

        section(
            "installation of recommended programs",
            f"recommended programs ({progtype})"
        )

        index: int; appname: str
        for index, appname in progindex.items():
            self.console.print(
                (
                    f"[bold cyan]{index:4}[/bold cyan] "
                    f"[bold]{appname}[/bold] -- "
                    f"{progdata.get(appname).get('sdesc')}" # type: ignore
                )
            )

        return uinput(
            self.console,
            "Input the number of applications to install",
            2
        )

    def install(self) -> tuple[list[list[str]], list[str]]:
        """For installation of recommended program selected by user."""

        t_fcmd: list[list[str]] = []
        t_rprog: list[str] = []

        # fprog_index -> flatpak programs index
        # rappsindex -> rpm programs index
        fprog_index: int; rprog_index: int

        #* FOR FLATPAK PROGRAMS
        #* appends the flatpak commands that needs to be executed in
        #* flatpak_cmd_list for a single execution of commands
        for fprog_index in self._enum_prog(
                self.FPROG_INDEX, self.FPROG_ARR, "flatpak"
            ):
            fapp_id: str = self.FPROG_ARR.get(
                    self.FPROG_INDEX.get(fprog_index) # type: ignore
                ).get("aid")
            install_cmd: list[str] = [
                    "flatpak",
                    "install",
                    "flathub",
                    fapp_id,
                    "--assumeyes"
                ]
            t_fcmd.append(install_cmd)


        #* FOR RPM PROGRAM
        #* appends the list of name of the selected rpm applications
        for rprog_index in self._enum_prog(
                self.RPROG_INDEX, self.RPROG_ARR, "rpm"
            ):
            rapp_id: str = self.RPROG_ARR.get( # type: ignore
                    self.RPROG_INDEX.get(rprog_index) # type: ignore
                ).get("aid")
            t_rprog.append(rapp_id)

        return t_fcmd, t_rprog
