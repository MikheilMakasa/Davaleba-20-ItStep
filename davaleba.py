class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def printLeafNodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.value, end=" ")
            self.printLeafNodes(node.left)
            self.printLeafNodes(node.right)

    def countEdges(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        left_edges = self.countEdges(node.left)
        right_edges = self.countEdges(node.right)
        return 1 + left_edges + right_edges


# Creating a binary tree
root_node = 1
binary_tree = BinaryTree(root_node)
binary_tree.root.left = TreeNode(2)
binary_tree.root.right = TreeNode(3)
binary_tree.root.left.left = TreeNode(4)
binary_tree.root.left.right = TreeNode(5)
binary_tree.root.right.left = TreeNode(6)
binary_tree.root.right.right = TreeNode(7)

# Leaf nodes
print("Leaf Nodes:")
binary_tree.printLeafNodes(binary_tree.root)
print()

# Count edges
edges_count = binary_tree.countEdges(binary_tree.root)
print(f"Number of edges: {edges_count}")

