import pytest

from exercises.arrays_hashing.two_sum.two_sum import two_sum


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # caso básico
        ([-3, 4, 3, 90], 0, [0, 2]),  # números negativos
        ([3, 2, 4], 6, [1, 2]),  # no usa el mismo elemento dos veces (3 + 3)
        ([3, 3], 6, [0, 1]),  # valores repetidos
        ([1, 2, 3], 7, []),  # sin solución
    ],
)
def test_two_sum(nums: list[int], target: int, expected: list[int]) -> None:
    assert two_sum(nums, target) == expected
