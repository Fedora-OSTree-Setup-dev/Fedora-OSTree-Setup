from argparse import ArgumentParser

from src.utils.shared.log.logger import Logger

class Cli:
    """Commandline interface of the program."""

    def __init__(self) -> None:
        self.log: Logger = Logger()

        self.parser: ArgumentParser = ArgumentParser(
                prog="ostree-setup",
                usage="ostree-setup [ARGUMENTS]",
                description=(
                        "A small program making the install of Fedora "
                        "Silverblue / Kionite easy. It lets you choose "
                        "what to install or set. "
                    )
            )
