# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        self.result = 0

        def dfs(node, currentSum):
            if node is None:
                return

            currentSum += node.val
            
            
            self.result += prefixSum.get(currentSum - targetSum, 0)
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)

            prefixSum[currentSum] -= 1

        dfs(root, 0)
        return self.result
            