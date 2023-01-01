from os import mkdir
from os.path import isdir, exists
from pathlib import Path
from json import load
from typing import NoReturn

from src.utils.conf.fetch_config import fetch_missing_config
from src.utils.shared.log.logger import Logger


class Conf:
    """For parsing of the config file as well as checking."""

    def __init__(self, log: Logger) -> None:
        self.CONF_PATH: str = f"{Path.home()}/.config/ostree_setup"
        self.CONF_LIST: list[str] = [
                "app_for_install", "app_for_removal", "ostree_setup"
            ]

        self.log: Logger = log

    def check_missing(self) -> NoReturn | None:
        """Checks the config file if missing or not, if missing fetch the
        original config file from the repository."""

        if not isdir(self.CONF_PATH):
            try:
                mkdir(self.CONF_PATH)
            except (PermissionError, OSError) as Err:
                self.log.logger(
                    "E", f"{Err}. Cannot make dir for {self.CONF_PATH}"
                )
                raise SystemExit

        conf_name: str
        for conf_name in self.CONF_LIST:
            if not exists(f"{self.CONF_PATH}/{conf_name}.json"):
                fetch_missing_config(self.log, conf_name, self.CONF_PATH)

        return None

    def load_conf(self) -> list[dict[str, str | dict[str, str]]] | NoReturn:
        """Load the config file, append it to list and return the list
        containing the values of config file."""

        try:
            parsed_conf: list[dict[str, str | dict[str, str]]] = []
            for conf_name in self.CONF_LIST:
                with open(
                        f"{self.CONF_PATH}/{conf_name}.json",
                        "r",
                        encoding="utf-8"
                    ) as t_conf:
                    parsed_conf.append(
                        load(t_conf)
                    )
        except (FileNotFoundError, PermissionError) as Err:
            self.log.logger(
                "I", f"{Err}. Can't open config file, run the program again."
            )
        else:
            return parsed_conf

        raise SystemExit
