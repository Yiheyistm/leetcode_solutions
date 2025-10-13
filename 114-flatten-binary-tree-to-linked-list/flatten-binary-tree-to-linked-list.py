# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        def dfs(node):
            if node and not node.left and not node.right:
                return node
            if not node:
                return None
            
            right = node.right
            if node.left:
                node.right = node.left
                end_node = dfs(node.left)
                node.left = None
                if right:
                    end_node.right = right
                else:
                    return end_node
            return dfs(right)

        dfs(root)
            
        