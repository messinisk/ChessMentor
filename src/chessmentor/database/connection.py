"""_summary_

Returns:
    _type_: _description_
"""

import sqlite3


def create_connection(address: str = ":memory:"):
    """_summary_

    Args:
        address (_type_, optional): _description_. Defaults to ":memory:".

    Returns:
        _type_: _description_
    """
    return sqlite3.connect(address)
