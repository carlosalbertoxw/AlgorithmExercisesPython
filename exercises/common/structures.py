"""Estructuras de datos compartidas entre ejercicios.

Definiciones estándar de LeetCode para listas enlazadas y árboles
binarios, con helpers para construirlas desde listas de Python
(útil en los tests).
"""

from collections import deque
from typing import Self


class ListNode:
    """Nodo de una lista enlazada simple."""

    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: list[int]) -> Self | None:
        """Construye una lista enlazada a partir de una lista de Python.

        >>> ListNode.from_list([1, 2, 3]).to_list()
        [1, 2, 3]
        >>> ListNode.from_list([]) is None
        True
        """
        head = None
        for val in reversed(values):
            head = cls(val, head)
        return head

    def to_list(self) -> list[int]:
        """Convierte la lista enlazada en una lista de Python."""
        values = []
        node: ListNode | None = self
        while node:
            values.append(node.val)
            node = node.next
        return values


class TreeNode:
    """Nodo de un árbol binario."""

    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, values: list[int | None]) -> Self | None:
        """Construye un árbol desde su recorrido por niveles (formato de LeetCode).

        `None` indica que no hay nodo en esa posición.

        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> root.val, root.left.val, root.right.left.val, root.right.right.val
        (3, 9, 15, 7)
        >>> TreeNode.from_list([]) is None
        True
        """
        if not values or values[0] is None:
            return None
        root = cls(values[0])
        pending = deque([root])
        children = iter(values[1:])
        while pending:
            node = pending.popleft()
            for side in ("left", "right"):
                val = next(children, None)
                if val is not None:
                    child = cls(val)
                    setattr(node, side, child)
                    pending.append(child)
        return root
