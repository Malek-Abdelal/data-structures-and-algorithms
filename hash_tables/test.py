import pytest
from hash_table import HashTable

def test_set_key_value():
    hashtable = HashTable()
    hashtable.set("name", "John")
    assert hashtable.get("name") == "John"

def test_retrieve_existing_key():
    hashtable = HashTable()
    hashtable.set("name", "John")
    assert hashtable.get("name") == "John"

def test_retrieve_nonexistent_key():
    hashtable = HashTable()
    assert hashtable.get("Malek") is None

def test_get_all_unique_keys():
    hashtable = HashTable()
    hashtable.set("name", "John")
    hashtable.set("age", 30)
    hashtable.set("city", "New York")
    
    keys = hashtable.keys()
    assert keys == ["name", "age", "city"]

def test_handle_collision():
    hashtable = HashTable(size=2)
    hashtable.set("name", "John")
    hashtable.set("age", 30)
    
    assert hashtable.get("name") == "John"
    assert hashtable.get("age") == 30

def test_retrieve_value_from_collision_bucket():
    hashtable = HashTable(size=2)
    hashtable.set("name", "John")
    hashtable.set("age", 30)
    
    assert hashtable.get("name") == "John"
    assert hashtable.get("age") == 30

def test_hash_key_within_range():
    hashtable = HashTable()
    key = "name"
    index = hashtable._HashTable__hash(key)
    assert 0 <= index < hashtable._HashTable__size

