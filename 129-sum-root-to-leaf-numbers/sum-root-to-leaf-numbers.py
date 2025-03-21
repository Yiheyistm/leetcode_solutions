# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, curr=''):
                nonlocal res
                if not node:
                    return
                curr += str(node.val)
                if not node.left and not node.right:
                    res += int(curr)
                    return
                traverse(node.left, curr)
                traverse(node.right, curr)
        traverse(root)
        return res

        