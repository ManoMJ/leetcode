# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        def dfs(node, len=0, before='ROOT'):
            if not node:
                return
            
            self.result = max(self.result, len)

            if before=='ROOT':
                dfs(node.left, len+1, 'LEFT')
                dfs(node.right, len+1, 'RIGHT')
            if before=='LEFT':
                dfs(node.left, 1, 'LEFT')
                dfs(node.right, len+1, 'RIGHT')
            if before=='RIGHT':
                dfs(node.left, len+1, 'LEFT')
                dfs(node.right, 1, 'RIGHT')
        dfs(root)
        return self.result
        