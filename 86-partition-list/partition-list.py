class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        min_head = max_head = None
        min_temp = max_temp = None

        curr = head
        while curr:
            currVal = curr.val
            if currVal < x:
                if min_head:
                    min_temp.next = curr
                    min_temp = min_temp.next
                else:
                    min_head = curr
                    min_temp = curr
                if not curr.next and max_temp: max_temp.next = None
            else :
                if max_head:
                    max_temp.next = curr
                    max_temp = max_temp.next
                else:
                    max_head = curr
                    max_temp = curr
                if not curr.next and min_temp: min_temp.next = None
                
            curr = curr.next
        if min_temp:
            min_temp.next = max_head
        else: return max_head

        return min_head