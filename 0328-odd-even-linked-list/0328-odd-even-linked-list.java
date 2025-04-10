/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode even_head = head.next;

        ListNode odd_ptr = head;
        ListNode even_ptr = head.next;

        while (odd_ptr.next != null && even_ptr.next != null) {
            odd_ptr.next = even_ptr.next;
            odd_ptr = odd_ptr.next;

            even_ptr.next = odd_ptr.next;
            even_ptr = even_ptr.next;
        }

        odd_ptr.next = even_head;

        return head;
    }
}