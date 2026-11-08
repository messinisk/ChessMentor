"""_summary_"""

from chessmentor.database.connection import create_connection


def test_database_created() -> None:
    """_summary_"""
    conn = create_connection()

    assert conn is not None
