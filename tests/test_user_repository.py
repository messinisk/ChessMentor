"""Tests for UserRepository."""

from chessmentor.database.connection import create_connection
from chessmentor.database.repositories.user_repository import  UserRepository
from chessmentor.database.schema import create_schema
from chessmentor.models.user import User


def setup_repo() -> UserRepository:
    """Create test repository."""

    conn = create_connection(":memory:")
    create_schema(conn)

    return UserRepository(conn)


def test_create_user() -> None:
    """Insert a user."""

    repo = setup_repo()

    user_id = repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    assert user_id > 0


def test_get_user() -> None:
    """Read user from database."""

    repo = setup_repo()

    user_id = repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    user = repo.get(user_id)

    assert user is not None
    assert user.username == "kostas"


def test_get_by_username() -> None:
    """Find user by username."""

    repo = setup_repo()

    repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    user = repo.get_by_username("kostas")

    assert user is not None
    assert user.username == "kostas"


def test_list_users() -> None:
    """List all users."""

    repo = setup_repo()

    repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    users = repo.list()

    assert len(users) == 1
    assert users[0].username == "kostas"
