# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stk = []
        dq = deque([(root, 0)])
        while dq:
            node, l = dq.popleft()
            if len(stk) <= l:
                stk.append([])
            stk[l].append(node.val)
            if node.left:
                dq.append((node.left, l + 1))
            if node.right:
                dq.append((node.right, l + 1))

        return stk
        