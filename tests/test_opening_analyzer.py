"""Opening analyzer tests."""


from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)

from chessmentor.knowledge.openings.analyzer import (
    OpeningAnalyzer,
)


def test_detect_giuoco_piano() -> None:
    """Detect Giuoco Piano."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bc4",
            "Bc5",
        ]
    )

    assert opening is not None
    assert opening.id == "giuoco_piano"

def test_detect_two_knights_defense() -> None:
    """Detect Two Knights Defense."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bc4",
            "Nf6",
        ]
    )

    assert opening is not None
    assert opening.id == "two_knights_defense"

def test_detect_modern_bishops_opening() -> None:
    """Detect Modern Bishop's Opening."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bc4",
            "Nf6",
            "d3",
        ]
    )

    assert opening is not None
    assert opening.id == "modern_bishops_opening"

def test_detect_giuoco_pianissimo() -> None:
    """Detect Giuoco Pianissimo."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "e4",
            "e5",
            "Nf3",
            "Nc6",
            "Bc4",
            "Bc5",
            "c3",
            "Nf6",
            "d3",
        ]
    )

    assert opening is not None
    assert opening.id == "giuoco_pianissimo"


def test_detect_unknown_opening() -> None:
    """Detect unknown opening."""

    analyzer = OpeningAnalyzer(
        OpeningCatalog(),
    )

    opening = analyzer.detect(
        [
            "a4",
            "h5",
        ]
    )

    assert opening is None