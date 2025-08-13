# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        lNodeVal = -1
        rNodeVal = -1
        cur = head
        totalNode = 0
        while cur:
            totalNode += 1
            if totalNode == k:
               lNodeVal = cur.val
            cur = cur.next

        # right side node found at totalNode - k + 1
        cur = head
        i = 1

        while i < totalNode - k + 1:
            cur = cur.next
            i += 1
        rNodeVal = cur.val

        cur = head
        i = 1
        cnt = 0 # to stop the loop if both are swapped
        while cur:
            if cnt == 2: break
            if i == k:
                cur.val = rNodeVal
                cnt += 1
            if totalNode - k + 1 == i:
                cur.val = lNodeVal
                cnt += 1
            cur = cur.next
            i += 1
 
        return head

        

        