import pytest
from linked_list.linked_list import Node, LinkedList

def test_empty_linked_list():
    new_list = LinkedList()
    actual = new_list.head
    expected = None
    assert actual == expected

def test_insert_node():
    new_list = LinkedList()
    new_list.insert("Inserted Node")
    actual = new_list.head.value
    expected = "Inserted Node"
    assert actual == expected

def test_first_node_is_head():      # !!!!
    new_list = LinkedList()
    new_list.insert("First Node")
    actual = new_list.head.value
    expected = "First Node"
    assert actual == expected

def test_insert_multiple_nodes():
    new_list = LinkedList()
    new_list.insert(1)
    new_list.insert(2)
    actual1 = new_list.includes(1)
    actual2 = new_list.includes(2)
    expected = True
    # nodes_num = 2
    # actual = LinkedList.counter
    # expected = nodes_num
    assert actual1, actual2 == expected

def test_value_exists():
    new_list = LinkedList()
    new_list.insert(10)
    actual = new_list.includes(10)
    expected = True
    assert actual == expected

def test_value_not_exist():
    new_list = LinkedList()
    actual = new_list.includes(8)
    expected = False
    assert actual == expected

def test_linked_list_values():
    new_list = LinkedList()
    new_list.insert('C')
    new_list.insert('B')
    new_list.insert('A')
    actual = new_list.to_string()
    expected = '{ A } -> { B } -> { C } -> NONE'
    assert actual == expected



@pytest.fixture(autouse=True)
def counter_reset():
    LinkedList.counter = 0

    

