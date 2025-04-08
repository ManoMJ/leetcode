from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sums = list([])
        queue = deque([(root, 0)])
        

        while queue:
            node, depth = queue.popleft()
            
            if len(sums) > depth:
                sums[depth][1] += node.val
            else:
                sums.append( [depth , node.val] )
            
            if node.left:
                queue.append( (node.left, depth+1 ))
            if node.right:
                queue.append( (node.right, depth+1 ))
      
        sums.sort(key=lambda x : x[1], reverse=True)
        
        return sums[0][0] + 1