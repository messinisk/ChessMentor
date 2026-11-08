"""Opening rules."""


def moves_match(
    game_moves: list[str],
    opening_moves: list[str],
) -> bool:
    """Check opening match."""

    if len(game_moves) < len(opening_moves):
        return False

    return (
        game_moves[: len(opening_moves)]
        == opening_moves
    )
