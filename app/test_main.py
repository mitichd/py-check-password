import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("A$imple123", True),
        ("H3llo#World", True),
        ("Str0ng&Pass", True),
        ("A1!minimum", True),
        ("VeryStr0ng#Pass", True),
        ("Ab1#5678901234", True),
        ("", False),
        ("Ab1#567", False),
        ("Ab1#5678901234567", False),
        ("password123$", False),
        ("PASSWORD123$", False),
        ("Password$$$", False),
        ("Password123", False),
        ("Passw%rd123", False),
        ("Пароль123!", False),
        ("Pass word1$", False),
        ("Pass,word1$", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
