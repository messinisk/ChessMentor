"""Here Opening model"""

from dataclasses import dataclass


@dataclass(slots=True)
class Opening:
    """Opening model"""
    id: str
    name_en: str
    name_el: str
    moves: list[str]
    eco: str | None = None
    parent: str | None = None
