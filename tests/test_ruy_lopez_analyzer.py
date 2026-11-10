from chessmentor.knowledge.openings.analyzer import (
    OpeningAnalyzer,
)

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)


def test_detect_ruy_lopez() -> None:
    """Detect Ruy Lopez."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bb5",
        ]
    )

    assert opening is not None
    assert opening.id == "ruy_lopez"

def test_detect_exchange_variation() -> None:
    """Detect Exchange Variation."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bb5",
            "a6",
            "Bxc6",
        ]
    )

    assert opening is not None
    assert opening.id == (
        "exchange_variation"
    )

def test_detect_open_defense() -> None:
    """Detect Open Defense."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bb5",
            "a6",
            "Ba4",
            "Nf6",
            "O-O",
            "Nxe4",
        ]
    )

    assert opening is not None
    assert opening.id == (
        "ruy_lopez_open_defense"
    )

def test_detect_closed_defense() -> None:
    """Detect Closed Defense."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bb5",
            "a6",
            "Ba4",
            "Nf6",
            "O-O",
            "Be7",
        ]
    )

    assert opening is not None
    assert opening.id == (
        "closed_ruy_lopez"
    )

