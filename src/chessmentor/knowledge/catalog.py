"""Knowledge catalog."""

from __future__ import annotations

import json
from pathlib import Path

from chessmentor.models.pattern import Pattern


class KnowledgeCatalog:
    """Load and provide access to chess patterns."""

    def __init__(
        self,
        knowledge_dir: str = "data/knowledge",
    ) -> None:
        self.knowledge_dir = Path(knowledge_dir)

    def _load_file(
        self,
        filename: str,
    ) -> list:
        """Load patterns from JSON file."""

        path = self.knowledge_dir / filename

        with path.open(
            encoding="utf-8",
        ) as handle:
            data = json.load(handle)

        return [
            Pattern(
                id=item["id"],
                category=item["category"],
                name_en=item["name_en"],
                name_el=item["name_el"],
                difficulty=item["difficulty"],
            )
            for item in data
        ]

    def load_tactics(self) -> list:
        """Load tactics patterns."""

        return self._load_file(
            "tactics.json",
        )

    def load_strategy(self) -> list:
        """Load strategy patterns."""

        return self._load_file(
            "strategy.json",
        )

    def load_all(self) -> list[Pattern]:
        """Load all patterns."""

        patterns: list[Pattern] = []

        patterns.extend(
            self.load_fundamentals()
        )

        patterns.extend(
            self.load_openings()
        )

        patterns.extend(
            self.load_tactics()
        )

        patterns.extend(
            self.load_strategy()
        )

        patterns.extend(
            self.load_endgames()
        )

        return patterns

    def get_by_id(
        self,
        pattern_id: str,
    ) -> Pattern | None:
        """Find pattern by ID."""

        for pattern in self.load_all():
            if pattern.id == pattern_id:
                return pattern

        return None

    def load_fundamentals(
        self,
    ) -> list[Pattern]:
        """Load fundamentals."""

        return self._load_file(
            "fundamentals.json",
        )


    def load_openings(
        self,
    ) -> list[Pattern]:
        """Load openings."""

        return self._load_file(
            "openings.json",
        )


    def load_endgames(
        self,
    ) -> list[Pattern]:
        """Load endgames."""

        return self._load_file(
            "endgames.json",
        )