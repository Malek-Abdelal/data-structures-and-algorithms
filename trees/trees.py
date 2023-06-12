class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Depth-first traversal: Pre-order
    def pre_order(self):
        values = []
        self.pre_order_helper(self.root, values)
        return values

    def pre_order_helper(self, node, values):
        if node is not None:
            values.append(node.value)
            self.pre_order_helper(node.left, values)
            self.pre_order_helper(node.right, values)

    # Depth-first traversal: In-order
    def in_order(self):
        values = []
        self.in_order_helper(self.root, values)
        return values

    def in_order_helper(self, node, values):
        if node is not None:
            self.in_order_helper(node.left, values)
            values.append(node.value)
            self.in_order_helper(node.right, values)

    # Depth-first traversal: Post-order
    def post_order(self):
        values = []
        self.post_order_helper(self.root, values)
        return values

    def post_order_helper(self, node, values):
        if node is not None:
            self.post_order_helper(node.left, values)
            self.post_order_helper(node.right, values)
            values.append(node.value)

    def find_maximum_value(self):
        if self.root is None:
            return None

        return self.find_maximum_value_helper(self.root)

    def find_maximum_value_helper(self, node):
        if node is None:
            return float('-inf')

        max_value = node.value
        left_max = self.find_maximum_value_helper(node.left)
        right_max = self.find_maximum_value_helper(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    # Add a node to the binary search tree
    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            self.add_node(self.root, new_node)

    def add_node(self, node, new_node):
        if new_node.value < node.value:
            if node.left is None:
                node.left = new_node
            else:
                self.add_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self.add_node(node.right, new_node)

    # Check if a value exists in the binary search tree
    def contains(self, value):
        return self.contains_node(self.root, value)

    def contains_node(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self.contains_node(node.left, value)

        return self.contains_node(node.right, value)
    

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(5)
    bst.add(7)

    print(bst.contains(5))         
    print(bst.contains(8))        

    print(bst.pre_order())        
    print(bst.in_order())          
    print(bst.post_order())       