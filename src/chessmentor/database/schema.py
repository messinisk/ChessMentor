"""Database schema creation."""

import sqlite3


def create_schema(conn: sqlite3.Connection) -> None:
    """Create all database tables."""

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,

            user_id INTEGER NOT NULL,

            white TEXT,
            black TEXT,

            result TEXT,

            opening TEXT,

            played_at TEXT,

            pgn TEXT NOT NULL,

            FOREIGN KEY(user_id)
                REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY,

            game_id INTEGER,

            accuracy REAL,

            mistakes INTEGER,

            blunders INTEGER,

            FOREIGN KEY(game_id)
                REFERENCES games(id)
        )
    """)

    conn.commit()
