from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


def title_banner(banner_text: str, banner_title: Optional[str] = None) -> None:
    """For displaying of title in major operation.

    Args:
        text -- main text to display
        title -- title of the banner
    """

    Console().print(
        Panel(
            Align(
                Text(
                    banner_text,
                    justify="center"
                ),
                vertical="middle",
                align="center"
            ),
            title=f"[bold]{banner_title}[/bold]"
        )
    )

    return None
