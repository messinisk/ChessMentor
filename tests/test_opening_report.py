from chessmentor.analysis.opening_report import (
    OpeningReport,
)

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)


def test_build_report() -> None:

    catalog = OpeningCatalog()

    opening = catalog.get_by_id(
        "italian_game",
    )

    assert opening is not None

    report = OpeningReport.build(
        opening,
    )

    assert "Italian Game" in report
    assert "C50" in report