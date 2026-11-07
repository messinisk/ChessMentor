"""PGN parser."""

from pathlib import Path

# pylint: disable=import-error
import chess.pgn  # type: ignore


def load_pgn(filename: str):
    """Load PGN game."""

    with Path(filename).open(encoding="utf-8") as handle:
        return chess.pgn.read_game(handle)
