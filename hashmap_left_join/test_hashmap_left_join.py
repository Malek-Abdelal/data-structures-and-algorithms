import pytest
from hashmap_left_join.hashmap_left_join import HashTable, left_join

def test_left_join_matching_keys():
    """
    Test left join with matching keys in both hashmaps.
    """
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap1.set("good", "nice")
    hashmap1.set("cat", "kitten")
    hashmap1.set("dog", "doggy")
    hashmap2.set("cat", "dog")
    hashmap2.set("good", "bad")
    hashmap2.set("name", "no_name")
    expected_result = [['good', 'nice', 'bad'], ['cat', 'kitten', 'dog'], ['dog', 'doggy', None]]
    assert left_join(hashmap1, hashmap2) == expected_result

def test_left_join_no_matching_keys():
    """
    Test left join with no matching keys in both hashmaps.
    """
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap1.set("good", "nice")
    hashmap1.set("cat", "kitten")
    hashmap1.set("dog", "doggy")
    hashmap2.set("diligent", "employed")
    hashmap2.set("guide", "usher")
    hashmap2.set("wrath", "anger")
    expected_result = [['good', 'nice', None], ['cat', 'kitten', None], ['dog', 'doggy', None]]
    assert left_join(hashmap1, hashmap2) == expected_result

def test_left_join_empty_hashmap2():
    """
    Test left join with an empty hashmap2.
    """
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap1.set("good", "nice")
    hashmap1.set("cat", "kitten")
    hashmap1.set("dog", "doggy")
    expected_result = [['good', 'nice', None], ['cat', 'kitten', None], ['dog', 'doggy', None]]
    assert left_join(hashmap1, hashmap2) == expected_result

def test_left_join_empty_hashmap1():
    """
    Test left join with an empty hashmap1.
    """
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap2.set("diligent", "employed")
    hashmap2.set("guide", "usher")
    hashmap2.set("wrath", "anger")
    expected_result = []
    assert left_join(hashmap1, hashmap2) == expected_result

def test_left_join_both_empty_hashmaps():
    """
    Test left join with both hashmaps being empty.
    """
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    expected_result = []
    assert left_join(hashmap1, hashmap2) == expected_result
