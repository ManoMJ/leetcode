# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        li = []
        pointer = head
        while pointer:
            li.append(pointer.val)
            pointer=pointer.next
        
        answer_head = ListNode(li.pop())
        answer_pointer = answer_head
        print(li)
        while li:
            new_node = ListNode(li.pop())
            answer_pointer.next = new_node
            answer_pointer = answer_pointer.next

        return answer_head