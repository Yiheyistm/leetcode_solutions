"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            while node:
                if not node.next and not node.child:
                    return node
                if node.child:
                    next_node = node.next
                    end_node = dfs(node.child)
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    end_node.next = next_node
                    if next_node:
                        next_node.prev = end_node
                        node = next_node
                    else:
                        return end_node 
                else:
                    node = node.next
                
        if not head:
            return head

        dfs(head)
        return head
        # Checker
        # curr = head
        # while curr.next:
        #     # print(curr.val)
        #     curr = curr.next
        # while curr:
        #     print(curr.val)
        #     curr = curr.prev
       

        