from chessmentor import ChessMentor # type: ignore


def test_import():
    cm = ChessMentor()

    assert cm is not None