# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cheating = []
        while head:
           cheating.append(head.val)
           head = head.next        

        mx_sum = float('-inf')
        n = len(cheating)
        for i in range(n // 2):
            mx_sum = max(mx_sum, cheating[i] + cheating[n-i-1])
        return mx_sum
        