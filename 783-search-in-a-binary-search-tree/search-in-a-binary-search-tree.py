# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def _search(node, val):
            if node.val == val:
                return node
            if val > node.val:
                if node.right:
                    return _search(node.right, val)
            elif val < node.val:
                if node.left:
                    return _search(node.left, val)
            else:
                return None
        return _search(root, val)
            
        