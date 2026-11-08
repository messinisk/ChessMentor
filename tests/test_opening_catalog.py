"""Opening catalog tests."""

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)


def test_load_openings() -> None:
    """Load openings."""

    catalog = OpeningCatalog()

    openings = catalog.load()

    assert len(openings) > 0


def test_find_italian_game() -> None:
    """Find Italian Game."""

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "italian_game",
    )

    assert opening is not None
    assert opening.eco == "C50"


def test_find_giuoco_piano() -> None:
    """Find Giuoco Piano."""

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "giuoco_piano",
    )

    assert opening is not None


def test_find_two_knights_defense() -> None:
    """Find Two Knights Defense."""

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "two_knights_defense",
    )

    assert opening is not None


def test_find_giuoco_pianissimo() -> None:
    """Find Giuoco Pianissimo."""

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "giuoco_pianissimo",
    )

    assert opening is not None
