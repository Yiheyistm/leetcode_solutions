# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        res = []
        ltr = True
        while dq:
            temp = deque()
            for i in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val) if ltr else temp.appendleft(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(list(temp))
            ltr = not ltr
        return res

        