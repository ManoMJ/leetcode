# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, head: Optional[ListNode]):
        nxt = head
        while nxt:
            print(f"{nxt.val} ->", end=" ")
            nxt = nxt.next
        print()
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        even = head.next
        odd = head
        nxt = None
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return head

        

