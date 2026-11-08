"""Fundamentals catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_fundamentals() -> None:
    """Load fundamentals."""

    catalog = KnowledgeCatalog()

    patterns = catalog.load_fundamentals()

    assert len(patterns) > 0


def test_find_development() -> None:
    """Find development."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "fundamental_development"
    )

    assert pattern is not None
    assert pattern.id == "fundamental_development"
    assert pattern.category == "fundamentals"