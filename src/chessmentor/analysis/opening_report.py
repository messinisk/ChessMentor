"""Opening report."""

from chessmentor.models.opening import Opening


class OpeningReport:
    """Opening report."""

    @staticmethod
    def build(
        opening: Opening,
    ) -> str:
        """Build opening report."""

        return (
            f"Opening: {opening.name_en}\n"
            f"ECO: {opening.eco}\n"
            f"Moves: {len(opening.moves)}"
        )
