from collections import deque

class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
                                                                        # Insert the values in to BST    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
                                                            # Depth First Search  (DFS)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
            
    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
                                                                # LEVEL ORDER TRAVERSAL (BFS) Breath First Search
    def level_order(self, root):                            
                                                                                    
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
            
                                                                    # Height of the BST      
    def height_of_bst(self,root):
        if root is None:
            return -1
        left_height=self.height_of_bst(root.left)
        right_height=self.height_of_bst(root.right)
        return 1+max(left_height,right_height)

# Create BST instance
bst = BST()
root = None

# Insert values into BST and update the root
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    root = bst.insert(root, val)
bst.insert(root,30)
# Perform traversals


print("Inorder Traversal of BST:")
bst.inorder(root)
print("\nPreorder Traversal of BST:")
bst.preorder(root)
print("\nPostorder Traversal of BST:")
bst.postorder(root)


height=bst.height_of_bst(root)
print("\n height of BST:",height)

print("\nLevel Order Traversal of BST:")
bst.level_order(root)







        