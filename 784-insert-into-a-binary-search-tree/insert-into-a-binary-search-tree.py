# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, val):
            if not node:
                return TreeNode(val)
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                return insert(node.right, val)
            elif val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                return insert(node.left, val)
        return insert(root, val)
        