from hash_tables import hash_table

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    def traverse_and_store_values(node, hashtable):
        if node:
            hashtable.set(node.value, True)
            traverse_and_store_values(node.left, hashtable)
            traverse_and_store_values(node.right, hashtable)

    hashtable = hash_table.HashTable()
    traverse_and_store_values(tree1, hashtable)

    common_values = []

    def find_common_values(node, hashtable):
        if node:
            if hashtable.has(node.value):
                common_values.append(node.value)
            find_common_values(node.left, hashtable)
            find_common_values(node.right, hashtable)

    find_common_values(tree2, hashtable)
    return set(common_values)

