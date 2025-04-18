# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def dfs(node):
            nonlocal max_sum
            if not node:
                return True, 0, float('inf'), float('-inf')
            l_bst, lf_sum,l_min, l_max = dfs(node.left)
            r_bst, rt_sum,r_min, r_max  = dfs(node.right)
            if  (l_max < node.val < r_min) and l_bst and r_bst:
                _sum = lf_sum + rt_sum + node.val
                max_sum = max(max_sum, _sum)
                return True, _sum, min(l_min, node.val), max(r_max, node.val)
            else:
                return False, 0, 0, 0

        
        dfs(root)
        return max_sum



        