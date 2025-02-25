# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def calc(l1, l2, q): 
            if not l1 and  not l2 and  not q:
                return None
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            sm = val_1 + val_2 + q
            q, r = divmod(sm, 10)
            node = ListNode(r)

            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None
            print(l1_next, l2_next ,q)
            node.next = calc(l1_next, l2_next, q)

            return node


        return calc(l1, l2, 0)

        
