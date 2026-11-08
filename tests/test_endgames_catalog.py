"""Endgames catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_endgames() -> None:
    """Load endgames."""

    catalog = KnowledgeCatalog()

    patterns = catalog.load_endgames()

    assert len(patterns) > 0


def test_find_lucena() -> None:
    """Find lucena."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "lucena"
    )

    assert pattern is not None
    assert pattern.category == "endgames"