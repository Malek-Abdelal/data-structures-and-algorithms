import pytest
from trees.trees import BinarySearchTree


def test_instantiate_empty_tree(empty_tree):
    assert empty_tree.root is None

def test_instantiate_single_root_node():
    tree = BinarySearchTree()
    tree.add(10)
    assert tree.root.value == 10
    assert tree.root.left is None
    assert tree.root.right is None

def test_add_left_and_right_child(populated_tree):
    root = populated_tree.root
    assert root.left.value == 5
    assert root.right.value == 15

def test_pre_order_traversal(populated_tree):
    expected = [10, 5, 3, 7, 15, 12, 80]
    assert populated_tree.pre_order() == expected

def test_in_order_traversal(populated_tree):
    expected = [3, 5, 7, 10, 12, 15, 80]
    assert populated_tree.in_order() == expected

def test_post_order_traversal(populated_tree):
    expected = [3, 7, 5, 12, 80, 15, 10]
    assert populated_tree.post_order() == expected

def test_contains_existing_value(populated_tree):
    assert populated_tree.contains(7) is True

def test_contains_non_existing_value(populated_tree):
    assert populated_tree.contains(100) is False

def test_get_max_value(populated_tree):
    expected = 80
    assert populated_tree.find_maximum_value() == expected

@pytest.fixture
def empty_tree():
    return BinarySearchTree()

@pytest.fixture
def populated_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(80)
    return tree