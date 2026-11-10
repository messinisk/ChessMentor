from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)
from chessmentor.knowledge.openings.tree import (
    OpeningTree,
)


def test_scotch_is_root() -> None:

    tree = OpeningTree(
        OpeningCatalog(),
    )

    assert tree.is_root(
        "scotch_game",
    )


def test_scotch_classical_parent() -> None:

    tree = OpeningTree(
        OpeningCatalog(),
    )

    parent = tree.get_parent(
        "scotch_game_classical",
    )

    assert parent is not None
    assert parent.id == "scotch_game"