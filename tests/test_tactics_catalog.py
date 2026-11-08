"""Tactics catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_tactics() -> None:
    """Load tactics."""

    catalog = KnowledgeCatalog()

    tactics = catalog.load_tactics()

    assert len(tactics) > 0


def test_find_fork() -> None:
    """Find fork."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "fork"
    )

    assert pattern is not None
    assert pattern.name_en == "Fork"


def test_find_pin() -> None:
    """Find pin."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "pin"
    )

    assert pattern is not None