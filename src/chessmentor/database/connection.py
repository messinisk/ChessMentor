"""Database connection."""

import sqlite3
from pathlib import Path


def create_connection(
    db_path: str = "data/database/chessmentor.db",
) -> sqlite3.Connection:
    """Create SQLite connection."""

    Path(db_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    return sqlite3.connect(db_path)
