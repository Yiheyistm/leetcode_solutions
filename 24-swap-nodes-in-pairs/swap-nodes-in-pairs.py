# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        dummy = ListNode()
        p = dummy
        while cur and cur.next:
            p.next = cur.next
            cur.next = p.next.next
            p.next.next = cur
            p = p.next.next
            cur = cur.next
        return dummy.next



        