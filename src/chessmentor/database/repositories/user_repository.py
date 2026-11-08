"""User repository."""

from sqlite3 import Connection

from chessmentor.models.user import User


class UserRepository:
    """User persistence layer."""

    def __init__(
        self,
        conn: Connection,
    ) -> None:
        self.conn = conn

    def create(
        self,
        user: User,
    ) -> int:
        """create"""

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                username,
                created_at
            )
            VALUES (
                ?, datetime('now')
            )
            """,
            (user.username,),
        )

        self.conn.commit()

        row_id = cursor.lastrowid

        if row_id is None:
            raise RuntimeError("Failed to create user.")

        return row_id

    def get(
        self,
        user_id: int,
    ) -> User | None:
        """get"""

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                username
            FROM users
            WHERE id = ?
            """,
            (user_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return User(
            id=row[0],
            username=row[1],
        )

    def get_by_username(self, username: str) -> User | None:
        """get_by_username"""

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, username
            FROM users
            WHERE username = ?
            """,
            (username,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return User(
            id=row[0],
            username=row[1],
        )

    def delete(self, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_
        """

    def list(self) -> list[User]:
        """list"""

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, username
            FROM users
            """
        )

        rows = cursor.fetchall()

        return [
            User(
                id=row[0],
                username=row[1],
            )
            for row in rows
        ]
