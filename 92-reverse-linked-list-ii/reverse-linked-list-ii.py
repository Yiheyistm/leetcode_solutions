# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr =  dummy
        rev = rev_head = None
        prev = None
        i = 0
        while curr:
            next = curr.next
            if i + 1 == left: 
                rev = curr # taking the node before the start of left because it helps after reversing the segment
                rev_head = curr.next # it helps for after finding node at right
            if left <= i <= right:
                curr.next = prev
                prev = curr
                
            curr = next
            if i == right:
                rev.next = prev
                rev_head.next = curr
                break
            i += 1
            
        return dummy.next

        

        