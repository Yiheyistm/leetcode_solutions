# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        if k > n: # Actually the questions says k <= n but in some testcase they give k > n
            return head
        else:
            curr =  head
            rev = dummy
            rev_head = None
            prev = None
            i = 0
            while curr:
                if i % k == 0:
                    rev_head = curr
                next = curr.next
                curr.next = prev
                prev = curr    
                curr = next
                if (i + 1) % k == 0:
                    rev.next = prev
                    rev_head.next = curr
                    rev = rev_head
                    prev = None
                    n -= k
                if k > n:break
                i += 1
            
        return dummy.next

        
        
        