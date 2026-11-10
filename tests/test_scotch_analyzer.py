from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)

from chessmentor.knowledge.openings.analyzer import (
    OpeningAnalyzer,
)


def test_detect_scotch_game() -> None:

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "d4",
        ]
    )

    assert opening is not None
    assert opening.id == "scotch_game"
