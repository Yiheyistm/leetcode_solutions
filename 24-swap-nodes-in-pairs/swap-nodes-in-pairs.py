# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        isSwaped = True
        dummy = ListNode(0)
        curr = head
        prev = dummy
        while curr:
            if isSwaped and curr.next:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = curr
                prev.next = temp

                prev = curr
                isSwaped = False
            else:
                isSwaped = True
                curr = curr.next
            
        return dummy.next

        