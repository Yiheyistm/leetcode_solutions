# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(l, r):
            if l > r: return None
            mid = (r + l) // 2

            left = buildTree(l, mid - 1)
            right = buildTree(mid + 1, r)
            return TreeNode(nums[mid], left, right)
        
        return buildTree(0, len(nums) -1)
                


        