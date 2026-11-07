"""Valid Parentheses (LeetCode #20).

Dada una cadena con paréntesis, corchetes y llaves, determina si
todos los símbolos abren y cierran en el orden correcto.
"""

# Cada símbolo de cierre mapea al de apertura que le corresponde.
_PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    """Devuelve True si los brackets de `s` están balanceados.

    Los caracteres que no son brackets se ignoran.

    Complejidad: O(n) en tiempo, O(n) en espacio.

    >>> is_valid("{[()]}")
    True
    >>> is_valid("([)]")
    False
    """
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in _PAIRS and (not stack or stack.pop() != _PAIRS[char]):
            return False
    return not stack
