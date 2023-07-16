import pytest
from stack_and_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_enqueue(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.stack1.top.value == 3

def test_dequeue(queue_instance_with_3_nodes_123):
    assert queue_instance_with_3_nodes_123.dequeue() == 1

def test_empty_after_multiple_dequeues(queue_instance_with_3_nodes_123):
    queue_instance_with_3_nodes_123.dequeue()
    queue_instance_with_3_nodes_123.dequeue()
    queue_instance_with_3_nodes_123.dequeue() 
    with pytest.raises(Exception):
        queue_instance_with_3_nodes_123.dequeue()

def test_instantiate():
    new_queue = PseudoQueue()
    assert isinstance(new_queue, PseudoQueue)

def test_empty_queue_pop_raise_Exeption():
    new_stack = PseudoQueue()
    with pytest.raises(Exception):
        queue_instance_with_3_nodes_123.dequeue()
    


@pytest.fixture
def queue_instance_with_3_nodes_123():
    new_queue = PseudoQueue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    return new_queue