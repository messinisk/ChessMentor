"""Knowledge catalog tests."""

from chessmentor.knowledge.catalog import (
    KnowledgeCatalog,
)


def test_load_all_patterns() -> None:
    """Load all patterns."""

    catalog = KnowledgeCatalog()

    patterns = catalog.load_all()

    assert len(patterns) > 0


def test_unknown_pattern() -> None:
    """Unknown pattern."""

    catalog = KnowledgeCatalog()

    pattern = catalog.get_by_id(
        "does_not_exist"
    )

    assert pattern is None

def test_debug_load_all():

    catalog = KnowledgeCatalog()

    ids = {
        pattern.id
        for pattern in catalog.load_all()
    }

    assert "fundamental_development" in ids
    assert "italian_game" in ids
    assert "lucena" in ids