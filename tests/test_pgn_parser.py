"""_summary_
    """

from chessmentor.pgn.parser import load_pgn

def test_parse_pgn():
    """_summary_
    """
    game = load_pgn("tests/data/game1.pgn")

    assert game is not None
