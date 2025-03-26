# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root, li = []):
        if not root.left and not root.right:
            li.append(root.val)
            return
        if root.left:
            self.traversal(root.left, li)
        if root.right:
            self.traversal(root.right, li)
    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []
        self.traversal(root1, leaf1)
        self.traversal(root2, leaf2)
        if leaf1 == leaf2:
            return True
        return False
        