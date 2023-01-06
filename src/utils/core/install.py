from typing import Any

from src.utils.shared.misc.uinput import uinput
from src.utils.shared.misc.section import section
from src.misc.alias import ProgData, ProgIndex



class Install:
    """For installation of the recommended programs."""

    def __init__(
            self, fp_data_arr: ProgData, rpm_data_arr: ProgData
        ) -> None:
        """
        Args:
            log -- instance of Logger
            fp_data_arr -- lists of the recommended applications
                including their application id (aid) and description
            rpm_data_arr -- lists of the recommended applications
                including their application id (aid) and description
        """

        self.fp_PROGARR: ProgData = fp_data_arr
        self.rpm_PROGARR: ProgData = rpm_data_arr

        self.fp_PROGIND: ProgIndex = { # ind: program id of flatpak applications
                ind: aid for ind, aid in zip(
                    range(len(self.fp_PROGARR.items())),
                    self.fp_PROGARR.keys()
                )
            }
        self.rpm_PROGIND: ProgIndex = { # ind: program id of flatpak applications
                ind: aid for ind, aid in zip(
                    range(len(self.rpm_PROGARR.items())),
                    self.rpm_PROGARR.keys()
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
            progindex -- ind of applications and their name
            progdata -- lists of the recommended applications including
                their application id (aid) and description
            progtype -- type of application, where flatpak or rpm
        """

        section(
            "installation of recommended programs",
            f"recommended programs ({progtype})"
        )

        ind: int; progname: str
        for ind, progname in progindex.items():
            self.console.print(
                (
                    f"[bold cyan]{ind:4}[/bold cyan] "
                    f"[bold]{progname}[/bold] -- "
                    f"{progdata.get(progname).get('sdesc')}" # type: ignore
                )
            )

        return uinput(
            self.console,
            "Input the number of applications to install",
            2
        )

    def install(self) -> tuple[list[list[str]], list[str]]:
        """For installation of recommended program selected by user."""

        t_fp_cmd: list[list[str]] = []
        t_rpm_prog: list[str] = []

        # fp_ind -> flatpak programs ind
        # rappsindex -> rpm programs ind
        fp_ind: int; rpm_ind: int

        #* FOR FLATPAK PROGRAMS
        #* appends the flatpak commands that needs to be executed in
        #* flatpak_cmd_list for a single execution of commands
        for fp_ind in self._enum_prog(
                self.fp_PROGIND, self.fp_PROGARR, "flatpak"
            ):
            fp_aid: str = self.fp_PROGARR.get(
                    self.fp_PROGIND.get(fp_ind) # type: ignore
                ).get("aid")
            install_cmd: list[str] = [
                    "flatpak",
                    "install",
                    "flathub",
                    fp_aid,
                    "--assumeyes"
                ]
            t_fp_cmd.append(install_cmd)


        #* FOR RPM PROGRAM
        #* appends the list of name of the selected rpm applications
        for rpm_ind in self._enum_prog(
                self.rpm_PROGIND, self.rpm_PROGARR, "rpm"
            ):
            r_aid: str = self.rpm_PROGARR.get( # type: ignore
                    self.rpm_PROGIND.get(rpm_ind) # type: ignore
                ).get("aid")
            t_rpm_prog.append(r_aid)

        return t_fp_cmd, t_rpm_prog
