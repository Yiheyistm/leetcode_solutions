# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        while True:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                break
            node = node.next
        
        
        