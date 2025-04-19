# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, stk):
            if not node:
                return []
            inorder(node.left, stk)
            stk.append(node.val)
            inorder(node.right,stk)
            return stk
        return inorder(root, [])

        