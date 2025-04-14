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
        dq = deque([root])
        elm = []
        level = 0
        while dq:
            elm.append([])
            for _ in range(len(dq)):
                node = dq.popleft()
                elm[level].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        return elm
                