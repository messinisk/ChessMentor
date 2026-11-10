"""Ruy Lopez tree tests."""

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)

from chessmentor.knowledge.openings.tree import (
    OpeningTree,
)


def test_ruy_lopez_is_root() -> None:
    """Ruy Lopez is root."""

    tree = OpeningTree(
        OpeningCatalog(),
    )

    assert tree.is_root(
        "ruy_lopez",
    )

def test_closed_defense_parent() -> None:
    """Closed Defense parent."""

    tree = OpeningTree(
        OpeningCatalog(),
    )

    parent = tree.get_parent(
        "closed_ruy_lopez",
    )

    assert parent is not None
    assert parent.id == "ruy_lopez"

def test_open_defense_parent() -> None:
    """Open Defense parent."""

    tree = OpeningTree(
        OpeningCatalog(),
    )

    parent = tree.get_parent(
        "ruy_lopez_open_defense",
    )

    assert parent is not None
    assert parent.id == "ruy_lopez"

def test_exchange_variation_parent() -> None:
    """Exchange Variation parent."""

    tree = OpeningTree(
        OpeningCatalog(),
    )

    parent = tree.get_parent(
        "exchange_variation",
    )

    assert parent is not None
    assert parent.id == "ruy_lopez"

def test_ruy_lopez_children() -> None:
    """Ruy Lopez children."""

    tree = OpeningTree(
        OpeningCatalog(),
    )

    children = tree.get_children(
        "ruy_lopez",
    )

    ids = {
        opening.id
        for opening in children
    }

    assert "closed_ruy_lopez" in ids
    assert "ruy_lopez_open_defense" in ids
    assert "exchange_variation" in ids

