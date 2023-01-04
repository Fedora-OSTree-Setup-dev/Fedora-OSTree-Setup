from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


def section(msg: str, title: str) -> None:
    """For displaying of title in major operation.

    Args:
        txt -- main txt to display
        title -- title of the section
    """

    Console().print(
        Panel(
            Align(
                Text(
                    msg.upper(),
                    justify="center"
                ),
                vertical="middle",
                align="center"
            ),
            title=f"[bold]{title.upper()}[/bold]"
        )
    )

    return None
