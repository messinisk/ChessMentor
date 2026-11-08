"""Openings catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_openings() -> None:
    """Load openings."""

    catalog = KnowledgeCatalog()

    patterns = catalog.load_openings()

    assert len(patterns) > 0


def test_find_italian_game() -> None:
    """Find Italian Game."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "italian_game"
    )

    assert pattern is not None
    assert pattern.category == "openings"