# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node, l, stk):
            if not node:
                return []
            if len(stk) <= l:
                stk.append([])
            stk[l].append(node.val)
            bfs(node.left, l + 1, stk)
            bfs(node.right, l + 1, stk)
            return stk
        return bfs(root, 0, [])
        