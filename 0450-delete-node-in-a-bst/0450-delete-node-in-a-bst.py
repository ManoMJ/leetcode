class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No child
            if not root.left and not root.right:
                return None
            # Case 2: One child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Two children
            else:
                # Find in-order successor (smallest in right subtree)
                successor = self.findMin(root.right)
                root.val = successor.val
                # Delete the successor recursively
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
