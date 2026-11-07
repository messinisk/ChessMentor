"""_summary_"""

from dataclasses import dataclass


@dataclass(slots=True)
class Game:  # pylint: disable=too-many-instance-attributes
    """Game"""

    id: int | None
    user_id: int
    event: str | None
    site: str | None
    white: str
    black: str
    result: str
    date: str | None
    opening: str | None
    pgn: str
