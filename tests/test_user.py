"""_summary_"""

from chessmentor.models.user import User


def test_create_user():
    """_summary_"""
    user = User(id=None, username="kostas")

    assert user.username == "kostas"
