"""Strategy catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_strategy() -> None:
    """Load strategy."""

    catalog = KnowledgeCatalog()

    patterns = catalog.load_strategy()

    assert len(patterns) > 0


def test_find_outpost() -> None:
    """Find outpost."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "outpost"
    )

    assert pattern is not None
    assert pattern.category == "strategy"