"""importer here"""

from chessmentor.models.game import Game
from chessmentor.pgn.parser import load_pgn


def import_pgn(filename: str):
    """Import PGN."""

    pgn_game = load_pgn(filename)

    if pgn_game is None:
        raise ValueError(f"Failed to load PGN: {filename}")

    return Game(
        id=None,
        user_id=1,
        white=str(pgn_game.headers.get("White", "")),
        black=str(pgn_game.headers.get("Black", "")),
        result=str(pgn_game.headers.get("Result", "")),
        date=str(pgn_game.headers.get("Date", "")),
        opening=None,
        event=None,
        site=None,
        pgn=str(pgn_game),
    )
