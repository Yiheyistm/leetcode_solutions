# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if node == None:
                return 0
            left_include = 0
            if node.left:
                left_include = dfs(node.left.left)+ dfs(node.left.right)
            right_include = 0
            if node.right:
                right_include = dfs(node.right.left) + dfs(node.right.right)

            include = node.val + left_include + right_include
            exclude = dfs(node.left)+dfs(node.right)
            return max(include, exclude)
        return dfs(root)
        