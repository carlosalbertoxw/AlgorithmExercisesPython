import pytest
from two_sum import two_sum

def test_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

def test_no_solution():
    assert two_sum([1, 2, 3], 7) == []

def test_pair_at_end():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_same_number_twice():
    assert two_sum([3, 3], 6) == [0, 1]
