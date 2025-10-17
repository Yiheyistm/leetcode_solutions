# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        isSwaped = False
        curr = head
        while curr:
            if not isSwaped and curr.next:
                curr_val = curr.val
                nxt_val = curr.next.val
                curr.val = nxt_val
                curr.next.val = curr_val
                curr = curr.next
                isSwaped = True
            else:
                curr = curr.next
                isSwaped = False
        return head

        