"""User model."""

from dataclasses import dataclass


@dataclass(slots=True)
class User:
    """Represents a ChessMentor user."""

    id: int | None
    username: str
