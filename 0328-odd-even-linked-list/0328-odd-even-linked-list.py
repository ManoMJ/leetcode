# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        even_head = head.next

        odd_ptr = head
        even_ptr = head.next
        
        while odd_ptr.next and even_ptr.next:
            odd_ptr.next = even_ptr.next
            even_ptr.next = odd_ptr.next.next
            odd_ptr = odd_ptr.next
            even_ptr = even_ptr.next
        
        odd_ptr.next = even_head

        return head