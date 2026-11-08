"""Pattern tests."""

from chessmentor.models.pattern import (
    Pattern,
)


def test_pattern_creation() -> None:
    """Create pattern."""

    pattern = Pattern(
        id="fork",
        category="tactics",
        name_en="Fork",
        name_el="Πιρούνι",
        difficulty=1,
    )

    assert pattern.id == "fork"
