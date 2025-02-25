# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head.next
        print(head.val)
        length = 0
        while pointer:
            length += 1
            pointer = pointer.next
        
        if length < 1:
            return None
        middle = int((length+1) / 2)
        
        current = head
        length = 0
        prev = None
        while length < middle:
            prev = current
            current = current.next
            length += 1
        
        prev.next = current.next

        return head