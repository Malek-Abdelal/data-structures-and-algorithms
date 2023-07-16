from insertion import insert, insertion_sort
import pytest

def test_insert():
    sorted_array = [1, 3, 5, 7]
    value = 4
    insert(sorted_array, value)
    assert sorted_array == [1, 3, 4, 5, 7]

def test_insertion_sort():
    input_array = [5, 2, 4, 6, 1, 3]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == [1, 2, 3, 4, 5, 6]

def test_insert_empty_sorted():
    sorted_array = []
    value = 2
    insert(sorted_array, value)
    assert sorted_array == [2]

def test_insertion_sort_single_element_input():
    input_array = [1]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == [1]

if __name__ == "__main__":
    test_insert()
    test_insert_empty_sorted()
    test_insertion_sort_single_element_input()
