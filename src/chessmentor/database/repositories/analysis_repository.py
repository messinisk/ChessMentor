"""Analysis repository."""


class AnalysisRepository:
    """Persistence layer for analysis."""

    def create(self, _analysis):
        """Create analysis."""
        raise NotImplementedError

    def get(self, _analysis_id):
        """Get analysis."""
        raise NotImplementedError

    def get_by_game(self, _game_id):
        """Get analysis by game."""
        raise NotImplementedError

    def delete(self, _analysis_id):
        """Delete analysis."""
        raise NotImplementedError
