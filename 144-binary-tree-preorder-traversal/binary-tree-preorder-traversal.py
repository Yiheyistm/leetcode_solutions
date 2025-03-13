# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def tranverse(node, stk):
            if not node: return stk
            stk.append(node.val)
            tranverse(node.left, stk)
            tranverse(node.right, stk)
            
            return stk

        return tranverse(root, [])

            
        