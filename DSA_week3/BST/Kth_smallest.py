from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
    def kth_smallest(self, root, k):
        self.count = 0
        self.kth_value = None

        def inorder(node):
            if not node or self.count >= k:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.kth_value = node.data
                return
            inorder(node.right)

        inorder(root)
        return self.kth_value


bst = BST()
root = None

values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    root = bst.insert(root, val)
bst.insert(root,30)

k = 4
kth_smallest_element = bst.kth_smallest(root, k)
print(f"\n{k}rd smallest element in BST:", kth_smallest_element)

