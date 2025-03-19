# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mx, mn):
            if not node:
                return mx - mn
        
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            left =  dfs(node.left,mx, mn)
            right =  dfs(node.right, mx, mn)
            return max(left, right)
 
        return dfs(root, root.val, root.val)
        
        