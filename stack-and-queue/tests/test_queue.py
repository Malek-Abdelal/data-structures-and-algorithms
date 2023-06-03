import pytest
from node.node import Node
from queue.queue import Queue

def test_enqueue(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.front.value == 1
    assert queue_instance_with_3_nodes_123.back.value == 3

def test_dequeue(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.dequeue() == 1

def test_peek(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.peek() == 1
    
def test_empty_after_multiple_dequeues(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.is_empty() == False
    queue_instance_with_3_nodes_123.dequeue()
    queue_instance_with_3_nodes_123.dequeue()
    queue_instance_with_3_nodes_123.dequeue() 
    assert queue_instance_with_3_nodes_123.is_empty() == True    

def test_instantiate():
    new_queue = Queue()
    assert isinstance(new_queue, Queue)
    assert new_queue.is_empty() == True

def test_empty_queue_peek_or_pop_raise_Exeption():
    new_stack = Queue()
    assert new_stack.dequeue() == "The queue is empty !"
    assert new_stack.peek() == "The queue is empty !"
    


@pytest.fixture
def queue_instance_with_3_nodes_123():
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    return new_queue