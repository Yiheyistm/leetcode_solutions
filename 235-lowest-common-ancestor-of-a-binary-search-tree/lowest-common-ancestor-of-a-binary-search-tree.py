# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findParent(c, node, stk):
            if not node:
                return
            stk.append(node)
            if c > node.val:
                return findParent(c, node.right, stk)
            elif c < node.val:
                return findParent(c, node.left, stk)
            return stk
        ans = findParent(q.val, root, [])
        ans2 = findParent(p.val, root, [])

        lw_parent = root
        for p1, p2 in zip(ans, ans2):
            if p1 == p2:
                lw_parent = p1
        return lw_parent
        