# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        no_node = 0
        def traverse(node):
            nonlocal no_node
            if not node:
                return 0, 0
            total_count = 1
            total_sum = node.val

            left_sum, l_count = traverse(node.left)
            total_count += l_count
            total_sum += left_sum

            right_sum, r_count = traverse(node.right)
            total_count += r_count
            total_sum += right_sum

            if total_sum // total_count == node.val:
                no_node += 1
            
            return total_sum, total_count 
        traverse(root)
        return no_node
        