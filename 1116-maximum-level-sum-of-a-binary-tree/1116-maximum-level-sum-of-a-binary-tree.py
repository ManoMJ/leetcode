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
        if not root:
            return 0

        q = deque([root])
        max_sum = root.val
        answer = 1
        cur_level = 1

        while q:
            q_len = len(q)
            cur_sum = 0

            for _ in range(q_len):
                node = q.popleft()
                cur_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if max_sum < cur_sum:
                max_sum = cur_sum
                answer = cur_level
            
            cur_level+= 1

        return answer
                
