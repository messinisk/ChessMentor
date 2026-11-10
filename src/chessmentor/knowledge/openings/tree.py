"""Opening tree."""

from chessmentor.knowledge.openings.catalog import (
    OpeningCatalog,
)
from chessmentor.models.opening import Opening


class OpeningTree:
    """Opening tree explorer."""

    def __init__(
        self,
        catalog: OpeningCatalog,
    ) -> None:
        self.catalog = catalog

    def get_children(
        self,
        opening_id: str,
    ) -> list[Opening]:
        """Get child openings."""

        return [
            opening
            for opening in self.catalog.load()
            if opening.parent == opening_id
        ]

    def get_parent(
        self,
        opening_id: str,
    ) -> Opening | None:
        """Get parent opening."""

        opening = self.catalog.get_by_id(
            opening_id,
        )

        if opening is None:
            return None

        if opening.parent is None:
            return None

        return self.catalog.get_by_id(
            opening.parent,
        )

    def is_root(
        self,
        opening_id: str,
    ) -> bool:
        """Check whether opening is root."""

        opening = self.catalog.get_by_id(
            opening_id,
        )

        if opening is None:
            return False

        return opening.parent is None
