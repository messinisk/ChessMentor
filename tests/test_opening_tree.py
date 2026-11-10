
from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)

from chessmentor.knowledge.openings.tree import OpeningTree

def test_giuoco_piano_parent() -> None:

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "giuoco_piano"
    )

    assert opening is not None
    assert opening.parent == "italian_game"

def test_two_knights_parent() -> None:

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "two_knights_defense"
    )

    assert opening is not None
    assert opening.parent == "italian_game"

def test_modern_bishop_parent() -> None:

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "modern_bishops_opening"
    )

    assert opening is not None
    assert opening.parent == (
        "two_knights_defense"
    )

def test_no_self_parent() -> None:

    catalog = OpeningCatalog()

    for opening in catalog.load():

        assert opening.id != opening.parent

def test_opening_schema() -> None:

    catalog = OpeningCatalog()

    for opening in catalog.load():

        assert opening.id
        assert opening.name_en
        assert opening.name_el

        assert opening.eco

        assert isinstance(
            opening.moves,
            list,
        )

        assert len(opening.moves) > 0

def test_italian_game_is_root() -> None:

    tree = OpeningTree(
        OpeningCatalog(),
    )

    assert tree.is_root(
        "italian_game",
    )

def test_italian_children() -> None:

    tree = OpeningTree(
        OpeningCatalog(),
    )

    children = tree.get_children(
        "italian_game",
    )

    ids = {
        opening.id
        for opening in children
    }

    assert "giuoco_piano" in ids
    assert "two_knights_defense" in ids
