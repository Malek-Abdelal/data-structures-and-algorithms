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

def test_append(linked_list_instance_with_3_nodes_123):
    assert linked_list_instance_with_3_nodes_123.head.next.next.value == 3
    assert linked_list_instance_with_3_nodes_123.head.next.next.next is None

def test_multible_append(linked_list_instance_with_3_nodes_123):
    linked_list_instance_with_3_nodes_123.append(4)
    assert linked_list_instance_with_3_nodes_123.head.next.next.next.value == 4
    assert linked_list_instance_with_3_nodes_123.head.next.next.next.next is None

def test_insert_before(linked_list_instance_with_3_nodes_123):
    linked_list_instance_with_3_nodes_123.insert_before(2,10)
    assert linked_list_instance_with_3_nodes_123.head.next.value == 10
    assert linked_list_instance_with_3_nodes_123.head.next.next.value == 2

def test_insert_before_first_node(linked_list_instance):
    linked_list_instance.insert(1)
    linked_list_instance.insert_before(1,0)
    assert linked_list_instance.head.value == 0
    assert linked_list_instance.head.next.value == 1

def test_insert_after(linked_list_instance_with_3_nodes_123):
    linked_list_instance_with_3_nodes_123.insert_after(2,10)
    assert linked_list_instance_with_3_nodes_123.head.next.value == 2
    assert linked_list_instance_with_3_nodes_123.head.next.next.value == 10

def test_insert_after_last_node(linked_list_instance_with_3_nodes_123):
    linked_list_instance_with_3_nodes_123.insert_after(3,10)
    assert linked_list_instance_with_3_nodes_123.head.next.next.value == 3
    assert linked_list_instance_with_3_nodes_123.head.next.next.next.value == 10





@pytest.fixture(autouse=True)
def counter_reset():
    LinkedList.counter = 0

@pytest.fixture
def linked_list_instance():
    return LinkedList()

@pytest.fixture
def linked_list_instance_with_3_nodes_123():
    new_linked_list = LinkedList(Node(1))
    new_linked_list.append(2)
    new_linked_list.append(3)
    return new_linked_list




    

