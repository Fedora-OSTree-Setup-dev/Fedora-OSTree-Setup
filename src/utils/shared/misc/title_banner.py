from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


def title_banner(banner_text: str, banner_title: str) -> None:
    """For displaying of title in major operation.

    Args:
        text -- main text to display
        title -- title of the banner
    """

    Console().print(
        Panel(
            Align(
                Text(
                    banner_text.capitalize(),
                    justify="center"
                ),
                vertical="middle",
                align="center"
            ),
            title=f"[bold]{banner_title.upper()}[/bold]"
        )
    )

    return None
