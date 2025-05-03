# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                val, node = lst.val, lst
                heappush(heap, (val,i, node))
                
        i = len(lists)
        dummy = ListNode()
        curr = dummy
        while heap:
            _,_, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val,i, node.next))
                i += 1
        return dummy.next
        