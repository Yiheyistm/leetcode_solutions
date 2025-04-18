# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, maxLeft, minRight):
            if not node:
                return True
            if not(maxLeft < node.val < minRight):
                return False
            return isBST(node.left, maxLeft, node.val) and isBST(node.right, node.val, minRight)
        return isBST(root, float('-inf'), float('inf'))
        