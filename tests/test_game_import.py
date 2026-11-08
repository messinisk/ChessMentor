from chessmentor.pgn.importer import import_pgn


def test_import_game():
    """_summary_"""
    game = import_pgn("tests/data/game1.pgn")

    assert game.white
    assert game.black
