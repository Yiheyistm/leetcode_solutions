# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                curr = TreeNode(val)
                root = curr
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                stack.append(curr.right)
            elif val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                stack.append(curr.left)
        return root
        