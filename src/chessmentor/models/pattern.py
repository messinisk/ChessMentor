"""Pattern model."""

from dataclasses import dataclass


@dataclass(slots=True)
class Pattern:
    """Knowledge pattern."""

    id: str

    category: str

    name_en: str
    name_el: str

    difficulty: int
