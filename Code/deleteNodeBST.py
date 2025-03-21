class TreeNode:
    def __init__(self, val=0, left=None, right=None): # define a node of BST
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self): # defines a BST
        self.root = None

    def insert(self, val): # create a BST
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        return root

    def delete(self, key): # deletion of a node
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, root, key):
        if not root:
            return root # base case empty tree

        # recursively find for target node to delete
        if key < root.val:
            root.left = self._deleteNode(root.left, key)
        elif key > root.val:
            root.right = self._deleteNode(root.right, key)

        else: # No or one child node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # two child node
            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._deleteNode(root.right, temp.val)

        return root

    def _minValueNode(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        self._inorder(self.root)
        print()

    # print left sub-tree first then right, in sorted manner
    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val, end=" ")
            self._inorder(root.right)

"""
        10
       /  \
      8    12
     / \   / \
    3   9 11 13
   / \       / \
  1   4     12 15
     /
    5
"""
# Example BST
bst = BST()
bst.insert(10)  # Root
bst.insert(8)   # Left child of 10
bst.insert(12)  # Right child of 10
bst.insert(3)   # Left child of 8
bst.insert(9)   # Right child of 8
bst.insert(1)   # Left child of 3
bst.insert(4)   # Right child of 3
bst.insert(5)   # Left child of 4
bst.insert(11)  # Left child of 12
bst.insert(13)  # Right child of 12
bst.insert(12)  # Left child of 13
bst.insert(15)  # Right child of 13

print("Inorder before deletion:")
bst.inorder()

bst.delete(5) # Leaf node deletion
bst.delete(4) # Delete a single child node
bst.delete(8)  # Deleting node with two children

print("Inorder after deletion:")
bst.inorder()
