# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        node = root
        parent = None

        while node:
            if node.val==key:
                break
            elif node.val > key:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        if not node:
            return root
        
        # 1 : 말단 노드
        if not node.left and not node.right:
            if not parent:
                return None
            elif parent.val > node.val:
                parent.left = None
            else:
                parent.right = None
        
        # 2 : 왼쪽 자식만 있는 경우
        elif node.left and not node.right:
            if not parent:
                root = node.left
            elif parent.val > node.val:
                parent.left = node.left
            else:
                parent.right = node.left
        # 3 : 오른쪽 자식이 있는 경우
        else:
            smaller = node.right
            smallerParent = node
            while smaller.left:
                smallerParent = smaller
                smaller = smaller.left
            if smallerParent.val > smaller.val:
                smallerParent.left = smaller.right
            else:
                smallerParent.right = smaller.right
            node.val = smaller.val
            
        
        return root
            
        
