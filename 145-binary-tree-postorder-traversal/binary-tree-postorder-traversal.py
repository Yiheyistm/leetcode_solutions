# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(node, stk):
            if not node:
                return stk
            postOrder(node.left, stk)
            postOrder(node.right, stk)
            stk.append(node.val)
            return stk
        return postOrder(root,[])


        