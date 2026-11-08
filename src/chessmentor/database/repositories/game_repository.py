"""_summary_"""


class GameRepository:
    """GameRepository"""

    def __init__(self, conn):
        self.conn = conn

    def create(self, game):
        """Create game."""

        raise NotImplementedError

    def get(self, game_id):
        """Get game."""

        raise NotImplementedError

    def delete(self, game_id):
        """delete game."""

        raise NotImplementedError

    def list_by_user(self, user_id):
        """list_by_user game."""

        raise NotImplementedError

    def count_by_user(self, user_id):
        """count_by_user game."""

        raise NotImplementedError
