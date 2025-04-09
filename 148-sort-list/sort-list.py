# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l, r):
            dummy = ListNode(0)
            trav = dummy
            while l and r:
                l_val = l.val
                r_val = r.val
                if l_val <= r_val:
                    l = l.next
                if r_val < l_val:
                    r = r.next
                trav.next = ListNode(min(l_val, r_val))
                trav = trav.next

            if not l and r:
                trav.next = r
            if not r and l:
                trav.next = l

            return dummy.next

        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        left = head
        right = slow.next
        slow.next = None
        return merge(self.sortList(left), self.sortList(right))


        
            

                

        