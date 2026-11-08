"""Opening analyzer."""
from chessmentor.knowledge.catalog import KnowledgeCatalog
from chessmentor.models.opening import Opening


class OpeningAnalyzer:
    """Opening analyzer."""

    def __init__(
        self,
        catalog: KnowledgeCatalog,
    ) -> None:
        self.catalog = catalog

    def detect(
        self,
        moves: list[str],
    ) -> Opening | None:
        """Detect opening."""

        return None
