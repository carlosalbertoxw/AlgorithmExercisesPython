import pytest
from is_valid import is_valid

def test_valid_cases():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("{[()()]}") == True
    assert is_valid("") == True

def test_invalid_cases():
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("(((") == False
    assert is_valid("({[})") == False
    assert is_valid("}") == False
    assert is_valid("(") == False
    assert is_valid("(()") == False

def test_edge_cases():
    assert is_valid("(((((((((())))))))))") == True
    assert is_valid("(((((((((()))))))))") == False
