"""Estructuras de datos compartidas entre ejercicios.

Definiciones estándar de LeetCode para listas enlazadas y árboles
binarios, con helpers para construirlas desde listas de Python
(útil en los tests).
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    """Nodo de una lista enlazada simple."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values: list[int]) -> Optional["ListNode"]:
        """Construye una lista enlazada a partir de una lista de Python."""
        head = None
        for val in reversed(values):
            head = ListNode(val, head)
        return head

    def to_list(self) -> list[int]:
        """Convierte la lista enlazada en una lista de Python."""
        values = []
        node: Optional[ListNode] = self
        while node:
            values.append(node.val)
            node = node.next
        return values


class TreeNode:
    """Nodo de un árbol binario."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
