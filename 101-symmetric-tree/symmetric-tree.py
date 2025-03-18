# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSimilar(node1, node2):
            if not node2 and not node1: return True
            if (node1 and not node2) or (not node1 and node2):return False
            
            node2.left, node2.right = node2.right, node2.left
            return (node1.val == node2.val) and \
            isSimilar(node1.left, node2.left) and isSimilar(node1.right, node2.right)

        return isSimilar(root.left, root.right)


        
        