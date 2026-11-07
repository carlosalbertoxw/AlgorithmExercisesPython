import pytest

from exercises.stacks.valid_parentheses.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "s",
    [
        "()",
        "()[]{}",
        "{[()()]}",
        "",
        "(((((((((())))))))))",
        "a",  # los caracteres que no son brackets se ignoran
        "(a + b) * [c]",
    ],
)
def test_valid(s: str) -> None:
    assert is_valid(s)


@pytest.mark.parametrize(
    "s",
    [
        "(]",
        "([)]",
        "(((",
        "({[})",
        "}",
        "(",
        "(()",
        "(((((((((()))))))))",
        "(a + b]",
    ],
)
def test_invalid(s: str) -> None:
    assert not is_valid(s)
