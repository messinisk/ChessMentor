"""Database initialization."""

from chessmentor.database.connection import (
    create_connection,
)
from chessmentor.database.schema import (
    create_schema,
)


def initialize_database() -> None:
    """Initialize database."""

    conn = create_connection()

    create_schema(conn)

    conn.close()
