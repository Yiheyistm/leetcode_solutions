# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque([root])
        res = []
        while dq:
            local_max = float('-inf')
            for _ in range(len(dq)):
                poped = dq.popleft()
                local_max = max(local_max, poped.val)
                if poped.left:
                    dq.append(poped.left)
                if poped.right:
                    dq.append(poped.right)
            res.append(local_max)
        return res

        