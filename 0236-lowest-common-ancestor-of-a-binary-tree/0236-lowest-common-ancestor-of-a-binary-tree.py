# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node or node.val==p.val or node.val==q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left if left else right

        return dfs(root)
