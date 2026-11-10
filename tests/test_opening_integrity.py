from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)


def test_opening_ids_are_unique() -> None:

    catalog = OpeningCatalog()

    openings = catalog.load()

    ids = [
        opening.id
        for opening in openings
    ]

    assert len(ids) == len(set(ids))

def test_all_openings_have_eco() -> None:

    catalog = OpeningCatalog()

    for opening in catalog.load():

        assert opening.eco

def test_all_openings_have_moves() -> None:

    catalog = OpeningCatalog()

    for opening in catalog.load():

        assert len(opening.moves) > 0

def test_parent_exists() -> None:

    catalog = OpeningCatalog()

    openings = catalog.load()

    ids = {
        opening.id
        for opening in openings
    }

    for opening in openings:

        if opening.parent is not None:

            assert opening.parent in ids

