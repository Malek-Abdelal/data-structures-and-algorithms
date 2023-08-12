from tree_intersection import tree_intersection
from collections import Counter
import pytest

def test_tree_intersection():

    tree5 = tree_intersection.TreeNode(5)
    tree5.left = tree_intersection.TreeNode(3)
    tree5.right = tree_intersection.TreeNode(5)
    tree5.left.left = tree_intersection.TreeNode(2)
    tree5.left.right = tree_intersection.TreeNode(4)

    tree6 = tree_intersection.TreeNode(5)
    tree6.left = tree_intersection.TreeNode(5)
    tree6.right = tree_intersection.TreeNode(8)
    tree6.left.left = tree_intersection.TreeNode(3)
    tree6.left.right = tree_intersection.TreeNode(8)

    common_values = tree_intersection.tree_intersection(tree5, tree6)
    assert len(common_values) == 2
    assert Counter(common_values)[5] == 1
    assert Counter(common_values)[8] == 0

