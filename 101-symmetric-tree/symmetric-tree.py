# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inverseTree(root):
            if not root:
                return
            root.left, root.right = inverseTree(root.right), inverseTree(root.left)
            return root

        return str(root) == str(inverseTree(root))
        