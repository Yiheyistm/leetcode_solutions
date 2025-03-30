# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def makeBalancedTree(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            left_node = makeBalancedTree(l, mid - 1) # mid - 1 because mid is root for the left and right node
            right_node = makeBalancedTree(mid + 1, r)
            return TreeNode(nums[mid], left_node, right_node)

        def makeArray(node, arr):
            if not node:return
            arr.append(node.val)
            makeArray(node.left, arr)
            makeArray(node.right, arr)
            return arr

        nums = makeArray(root, [])
        nums.sort()
        return makeBalancedTree(0, len(nums) - 1)
        
        