# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head = head
        even_head = head.next
        evn = even_head
        while evn and evn.next:
            odd_head.next = evn.next
            odd_head = odd_head.next
            evn.next = odd_head.next
            evn = evn.next
        odd_head.next = even_head
        return head
        