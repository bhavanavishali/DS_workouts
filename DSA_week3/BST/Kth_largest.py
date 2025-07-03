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
    
    def kth_largest(self, root, k):
        self.count = 0
        self.kth_value = None

        def reverse_inorder(node):
            if not node or self.count >= k:
                return
            reverse_inorder(node.right)
            self.count += 1
            if self.count == k:
                self.kth_value = node.data
                return
            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.kth_value

                                                            



bst = BST()
root = None

values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    root = bst.insert(root, val)
bst.insert(root,30)

k = 2
kth_largest_element = bst.kth_largest(root, k)
print(f"\n{k}rd largest element in BST:", kth_largest_element)



