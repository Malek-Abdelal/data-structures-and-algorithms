import pytest
from node.node import Node
from stack.stack import Stack

def test_push(stack_instance_with_3_nodes_123):
    assert stack_instance_with_3_nodes_123.top.value == 3

def test_pop(stack_instance_with_3_nodes_123):
    assert stack_instance_with_3_nodes_123.pop() == 3
    
def test_empty_after_multiple_pops(stack_instance_with_3_nodes_123):
    assert stack_instance_with_3_nodes_123.is_empty() == False
    stack_instance_with_3_nodes_123.pop()
    stack_instance_with_3_nodes_123.pop()
    stack_instance_with_3_nodes_123.pop() 
    assert stack_instance_with_3_nodes_123.is_empty() == True    

def test_peek(stack_instance_with_3_nodes_123):
    assert stack_instance_with_3_nodes_123.peek() == 3

def test_instantiate():
    new_stack = Stack()
    assert isinstance(new_stack, Stack)
    assert new_stack.is_empty() == True

def test_empty_stack_peek_or_pop_raise_Exeption():
    new_stack = Stack()
    assert new_stack.pop() == "The stack is empty !"
    assert new_stack.peek() == "The stack is empty !"
    


@pytest.fixture
def stack_instance_with_3_nodes_123():
    new_stack = Stack(Node(1))
    new_stack.push(2)
    new_stack.push(3)
    return new_stack