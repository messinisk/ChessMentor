"""Tests for GameRepository."""

import pytest

from chessmentor.database.connection import (
    create_connection,
)
from chessmentor.database.repositories.game_repository import (
    GameRepository,
)
from chessmentor.database.repositories.user_repository import (
    UserRepository,
)
from chessmentor.database.schema import (
    create_schema,
)
from chessmentor.models.game import Game
from chessmentor.models.user import User


@pytest.fixture
def setup_repo():
    """Create repositories."""

    conn = create_connection(":memory:")
    create_schema(conn)

    return (
        UserRepository(conn),
        GameRepository(conn),
    )


@pytest.fixture
def test_create_game() -> None:
    """Insert game."""

    user_repo, game_repo = setup_repo()

    user_id = user_repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    game_id = game_repo.create(
        Game(
            id=None,
            user_id=user_id,
            white="Kostas",
            black="Stockfish",
            result="1-0",
            date="2026.11.07",
            opening="Italian Game",
            event=None,
            site=None,
            pgn="1.e4 e5",
        )
    )

    assert game_id > 0


@pytest.fixture
def test_get_game() -> None:
    """Read game."""

    user_repo, game_repo = setup_repo()

    user_id = user_repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    game_id = game_repo.create(
        Game(
            id=None,
            user_id=user_id,
            white="Kostas",
            black="Stockfish",
            result="1-0",
            date="2026.11.07",
            opening="Italian Game",
            event=None,
            site=None,
            pgn="1.e4 e5",
        )
    )

    game = game_repo.get(game_id)

    assert game is not None
    assert game.white == "Kostas"


@pytest.fixture
def test_list_games_by_user() -> None:
    """List user games."""

    user_repo, game_repo = setup_repo()

    user_id = user_repo.create(
        User(
            id=None,
            username="kostas",
        )
    )

    game_repo.create(
        Game(
            id=None,
            user_id=user_id,
            white="Kostas",
            black="Stockfish",
            result="1-0",
            date="2026.11.07",
            opening="Italian Game",
            event=None,
            site=None,
            pgn="1.e4 e5",
        )
    )

    games = game_repo.list_by_user(user_id) # assignment-from-no-return

    assert len(games) > 1
