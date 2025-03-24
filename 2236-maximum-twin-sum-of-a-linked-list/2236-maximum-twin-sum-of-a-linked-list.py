# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        second_head = head
        nxt = head.next
        if not nxt.next:
            return head.val + nxt.val

        while nxt.next:
            second_head = second_head.next
            nxt = nxt.next.next
        second_head = second_head.next
        
        prev = None
        current = second_head
        while nxt:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        second_head = prev

        first_ptr = head
        second_ptr = second_head
        answer = 0
        while first_ptr and second_ptr:
            answer = max(first_ptr.val + second_ptr.val, answer)
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        return answer
