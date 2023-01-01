from typing import Any

from rich.console import Console


def uinput(console: Console, msg: str, qtype: int) -> Any:
    """Takes user input and return the evaluated output.

    Args:
        console -- Console instance
        msg -- question to ask the user
        qtype -- question type, whether y/N, string input or number input
            1 is yes or no input
            2 is number/list input
            3 is for string or char input

    Returns:
        The evaluated input based on the user response, e.g.:
            y -> True
            N -> False
            1, 2, 3 -> list[int]
    """

    match qtype:
        case 1:
            console.print(
                f"{msg} [bold][[green]y[/green]/[red]N[/red]][/bold]", end=" "
            )
            if input().lower().strip() == "y":
                return True
        case 2:
            console.print(
                (
                    f"{msg} [bold][NUMBER/LIST INPUT"
                    ", separate by comma ','][/bold]"
                ), end=" "
            )
            items: str = input()
            return [int(item) for item in items.strip().split(",")]
        case 3:
            console.print(
                (
                    f"{msg} [bold][CHAR/STRING INPUT"
                    ", separate by comma ','][/bold]"
                ), end=" "
            )
            return input()

    return False
