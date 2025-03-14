# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr
            if val > curr.val and curr.right:
                stack.append(curr.right)
            elif val < curr.val and curr.left:
                stack.append(curr.left)
        return None
        

            
        