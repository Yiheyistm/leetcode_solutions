# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        left = head
        right = prev
        mx_sum = float('-inf')
        while right:
            mx_sum = max(left.val + right.val, mx_sum)
            left = left.next
            right = right.next

        return mx_sum
        