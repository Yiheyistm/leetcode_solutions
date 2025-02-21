# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        trv = head
        while trv.next:
            if trv.val == trv.next.val:
                trv.next = trv.next.next
            else:
                trv = trv.next
        return head
        