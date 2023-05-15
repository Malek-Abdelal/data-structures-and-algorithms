import pytest
from linked_list.linked_list import Node, LinkedList

def test_empty_linked_list(linked_list_instance):
    actual = linked_list_instance.head
    expected = None
    assert actual == expected

def test_insert_node(linked_list_instance):
    linked_list_instance.insert("Inserted Node")
    actual = linked_list_instance.head.value
    expected = "Inserted Node"
    assert actual == expected

def test_first_node_is_head(linked_list_instance):    
    linked_list_instance.insert("First Node")
    actual = linked_list_instance.head.value
    expected = "First Node"
    assert actual == expected

def test_insert_multiple_nodes(linked_list_instance):
    linked_list_instance.insert(1)
    linked_list_instance.insert(2)
    actual1 = linked_list_instance.includes(1)
    actual2 = linked_list_instance.includes(2)
    expected = True
    assert actual1, actual2 == expected

def test_value_exists(linked_list_instance):
    linked_list_instance.insert(10)
    actual = linked_list_instance.includes(10)
    expected = True
    assert actual == expected

def test_value_not_exist(linked_list_instance):
    actual = linked_list_instance.includes(8)
    expected = False
    assert actual == expected

def test_linked_list_values(linked_list_instance):
    linked_list_instance.insert('C')
    linked_list_instance.insert('B')
    linked_list_instance.insert('A')
    actual = linked_list_instance.to_string()
    expected = '{ A } -> { B } -> { C } -> NONE'
    assert actual == expected



@pytest.fixture(autouse=True)
def counter_reset():
    LinkedList.counter = 0

@pytest.fixture
def linked_list_instance():
    return LinkedList()




    

