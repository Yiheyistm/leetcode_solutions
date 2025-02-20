# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        temp_merge = ListNode()
        merge = temp_merge
        while list1 and list2:
            if list1.val <= list2.val:
                temp_merge.next = list1
                temp_merge = temp_merge.next
                if not list1.next and list2:
                    temp_merge.next = list2
                    break
                list1 = list1.next
            else:
                temp_merge.next = list2
                temp_merge = temp_merge.next
                if not list2.next and list1:
                    temp_merge.next = list1
                    break
                list2 = list2.next
    

        return merge.next

        