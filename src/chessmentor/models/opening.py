"""Here Opening model"""

from dataclasses import dataclass


@dataclass(slots=True)
class Opening:
    """Opening model"""
    id: str

    name_en: str
    name_el: str

    eco: str

    moves: list[str]
    parent: str | None = None
