from typing import NoReturn, Optional

from requests import get

from src.utils.shared.log.logger import Logger


def fetch_missing_config(
        log: Logger,
        conf_name: str,
        CONF_PATH: str,
        conf_links: Optional[dict[str, str]] = None
    ) -> None | NoReturn:
    """Downloads the original config file from github if not found.

    Args:
        log -- instance of Logger
        conf_name -- name of the missing config
        CONF_PATH -- path of the config file
        conf_links -- links of config files
    """

    if not conf_links:
        conf_links = {
                "app_for_install": (
                        "https://raw.githubusercontent.com/iaacornus/Fedora-"
                        "OSTree-Setup/devel/config/app_for_install.json"
                    ),
                "app_for_removal": (
                        "https://raw.githubusercontent.com/iaacornus/Fedora-"
                        "OSTree-Setup/devel/config/app_for_removal.json"
                    ),
                "ostree_setup": (
                        "https://raw.githubusercontent.com/iaacornus/Fedora-"
                        "OSTree-Setup/devel/config/ostree_setup.json"
                    )
            }

    attempt: int
    for attempt in range(3):
        try:
            log.logger(
                "I", f"Fetching the config file ({conf_name}) from Github."
            )
            if not (conf_link := conf_links.get(conf_name)):
                log.logger(
                    "E", f"Cannot fetch the config: {conf_name}, aborting ..."
                )
                raise SystemExit

            with get(conf_link, stream=True) as d_file:
                with open(
                        f"{CONF_PATH}/{conf_name}.json", "wb"
                    ) as conf_file:
                    for chunk in d_file.iter_content(chunk_size=1024):
                        if chunk:
                            conf_file.write(chunk)
        except (ConnectionError, IOError, PermissionError) as Err:
            if attempt < 2:
                continue

            log.logger(
                "E", f"{Err}. Cannot download {conf_name}, aborting ..."
            )
        else:
            log.logger("I", f"Sucessfully fetched: {conf_name}.")
            return None

    raise SystemExit

