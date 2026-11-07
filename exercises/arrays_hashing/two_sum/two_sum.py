"""Two Sum (LeetCode #1).

Dado un arreglo de enteros y un objetivo, encuentra los índices de
los dos números que suman el objetivo.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Devuelve los índices [i, j] (i < j) tales que nums[i] + nums[j] == target.

    Si no existe solución devuelve una lista vacía.

    Usa un diccionario valor -> índice para encontrar el complemento
    de cada número en una sola pasada.

    Complejidad: O(n) en tiempo, O(n) en espacio.

    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
