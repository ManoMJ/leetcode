# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None
        current = head
        
        while current:
            next_node = current.next  # 1) Temporarily store the next node
            current.next = prev       # 2) Reverse the pointer
            prev = current            # 3) Move 'prev' forward
            current = next_node       # 4) Move 'current' forward

        return prev  # 'prev' now points to the new head of the reversed list