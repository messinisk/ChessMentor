"""Opening analyzer."""

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)
from chessmentor.knowledge.openings.rules import (
    moves_match,
)
from chessmentor.models.opening import Opening


class OpeningAnalyzer:
    """Opening analyzer."""

    def __init__(
        self,
        catalog: OpeningCatalog,
    ) -> None:
        self.catalog = catalog

    def detect(
    self,
    moves: list[str],
) -> Opening | None:
        """Detect opening."""

        best_match: Opening | None = None

        for opening in self.catalog.load():

            if moves_match(
                moves,
                opening.moves,
            ):

                if (
                    best_match is None
                    or len(opening.moves)
                    > len(best_match.moves)
                ):
                    best_match = opening

        return best_match
