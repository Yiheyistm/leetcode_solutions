# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def possibleDepth(node, curr_depth):
            if not node: 
                return curr_depth
            left_child = possibleDepth(node.left, curr_depth + 1)
            right_child = possibleDepth(node.right, curr_depth + 1)
            return max(left_child, right_child)
            
        return possibleDepth(root, 0)




        