"""Opening recognition rules."""


def moves_match(
    game_moves: list[str],
    opening_moves: list[str],
) -> bool:
    """Check whether a game follows an opening."""

    if len(game_moves) < len(opening_moves):
        return False

    return (
        game_moves[: len(opening_moves)]
        == opening_moves
    )
