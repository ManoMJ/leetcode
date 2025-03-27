# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxTraverse(root, mx):
            if root is None:
                return 0
            
            mx = max(root.val, mx)
            result = 0
            if mx == root.val:
                result = 1
            if root:
                print(root.val)
            return maxTraverse(root.left, mx) + maxTraverse(root.right, mx) + result

        if not root:
            return 0
        return maxTraverse(root, root.val)