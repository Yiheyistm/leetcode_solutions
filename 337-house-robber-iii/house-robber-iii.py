# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            l_inc, l_ex = dfs(node.left)
            r_inc, r_ex = dfs(node.right)
            include = node.val + l_ex + r_ex
            exclude = max(l_inc, l_ex) + max(r_inc, r_ex)
            return include, exclude

        inc, exc = dfs(root)
        return max(inc, exc)
        