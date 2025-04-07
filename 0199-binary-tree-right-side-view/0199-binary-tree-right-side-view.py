from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        q = deque([(root, 0)])
        dic = defaultdict(list)
        
        result = []
        while q:
            top, depth = q.popleft()
            dic[depth].append(top.val)

            if top.left:
                q.append( (top.left, depth+1) )
            if top.right:
                q.append( (top.right, depth+1) )

        for k in dic.keys():
            result.append(dic[k][-1])
        return result