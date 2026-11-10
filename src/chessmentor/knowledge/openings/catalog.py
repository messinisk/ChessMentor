"""Opening catalog."""

from __future__ import annotations

import json
from pathlib import Path

from chessmentor.models.opening import Opening


class OpeningCatalog:
    """Opening catalog."""

    def __init__(
        self,
        path: str = "data/knowledge/openings.json",
    ) -> None:
        self.path = Path(path)

    def load(self) -> list[Opening]:
        """Load openings."""

        with self.path.open(
            encoding="utf-8",
        ) as handle:
            data = json.load(handle)

        return [
            Opening(
                id=item["id"],
                name_en=item["name_en"],
                name_el=item["name_el"],
                eco=item["eco"],
                moves=item["moves"],
                parent=item.get("parent"),
            )
            for item in data
        ]

    def get_by_id(
        self,
        opening_id: str,
    ) -> Opening | None:
        """Get opening by id."""

        for opening in self.load():
            if opening.id == opening_id:
                return opening

        return None
