# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        odd = head
        even = head.next

        if not even:
            return None

        while even.next and even.next.next:
            odd = odd.next
            even = even.next.next

        odd.next = odd.next.next

        return head