# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr = res
        q = 0
        while l1 and l2:
            sm = l1.val + l2.val + q
            if sm >= 10:
                q, r = divmod(sm, 10)
                node = ListNode(r)
            else:
                node = ListNode(sm)
                q = 0
            curr.next = node
            curr = node
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            trav = l1 or l2
            while trav:
                sm = trav.val + q
                if sm >= 10:
                    q, r = divmod(sm, 10)
                    node = ListNode(r)
                else:
                    node = ListNode(sm)
                    q = 0
                trav = trav.next
                curr.next = node
                curr = node
        if q:
            curr.next = ListNode(q)
            curr = curr.next
        return res.next


        
