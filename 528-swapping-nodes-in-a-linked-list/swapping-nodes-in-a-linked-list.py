# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        lNode, lPrev = None, dummy
        cur = head
        totalNode = 0
        while cur:
            totalNode += 1
            if totalNode + 1 == k:
               lPrev = cur
            if totalNode == k:
               lNode = cur
            cur = cur.next
        # right side node found at totalNode - k + 1
        rNode, rPrev = None, None
        cur = dummy
        i = 1

        while i < totalNode - k +1:
            cur = cur.next
            i += 1
        rPrev = cur
        rNode = cur.next
        
        lPrev.next = rNode
        rPrev.next = lNode
        rNodeNext = rNode.next
        rNode.next = lNode.next
        lNode.next = rNodeNext

        return dummy.next

        

        