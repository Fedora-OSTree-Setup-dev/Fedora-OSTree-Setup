from typing import NewType


AppData = NewType("AppData", dict[str, dict[str, str]])
AppIndex = NewType("AppIndex", dict[int, str])
