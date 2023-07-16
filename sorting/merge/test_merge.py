import pytest
from merge import mergesort

def test_mergesort_empty_list():
    arr = []
    mergesort(arr)
    assert arr == []

def test_mergesort_sorted_list():
    arr = [1, 2, 3, 4, 5]
    mergesort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    mergesort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_mergesort_random_list():
    arr = [4, 2, 1, 5, 3]
    mergesort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_mergesort_duplicate_values():
    arr = [3, 1, 2, 2, 1, 3]
    mergesort(arr)
    assert arr == [1, 1, 2, 2, 3, 3]
