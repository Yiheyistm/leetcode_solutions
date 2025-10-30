# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        less = ListNode()
        greater = ListNode()
        ls = less
        gr = greater
        while head:
            if head.val >= x:
                gr.next = head
                gr = gr.next
            else:
                ls.next = head
                ls = ls.next
            head = head.next
        gr.next = None
        ls.next = greater.next
        return less.next

        