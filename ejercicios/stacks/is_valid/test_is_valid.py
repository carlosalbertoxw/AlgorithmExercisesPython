from ejercicios.stacks.is_valid.is_valid import is_valid

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


def test_non_bracket_characters_are_ignored():
    assert is_valid("a") == True
    assert is_valid("(a + b) * [c]") == True
    assert is_valid("(a + b]") == False
