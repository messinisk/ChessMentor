"""Catalog lookup tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_find_fork() -> None:
    """Find fork pattern."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id("fork")

    assert pattern is not None
    assert pattern.name_en == "Fork"
