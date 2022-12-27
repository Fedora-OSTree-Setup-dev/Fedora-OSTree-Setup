from typing import NoReturn

from requests import get

from src.utils.log.logger import Logger


def fetch_missing_config(
        log: Logger, conf_name: str, CONF_PATH: str
    ) -> None | NoReturn:
    """Downloads the original config file from github if not found.

    Args:
        log -- instance of Logger
        conf_name -- name of the missing config
        CONF_PATH -- path of the config file
    """

    conf_link: str = ""

    trial: int
    for trial in range(3):
        try:
            log.logger(
                "I", "Fetching the missing config file from Github."
            )
            with get(conf_link, stream=True) as d_file:
                with open(
                        f"{CONF_PATH}/{conf_name}", "wb"
                    ) as conf_file:
                    for chunk in d_file.iter_content(chunk_size=1024):
                        if chunk:
                            conf_file.write(chunk)
        except (ConnectionError, IOError, PermissionError) as Err:
            if trial < 2:
                continue

            log.logger(
                "E", f"{Err}. Cannot download {conf_name}, aborting ..."
            )
        else:
            log.logger("I", f"Sucessfully fetched: {conf_name}.")
            return None

    raise SystemExit

