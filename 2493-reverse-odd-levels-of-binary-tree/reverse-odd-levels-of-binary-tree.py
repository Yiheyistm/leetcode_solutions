# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dq = deque([root])
        level = 0

        while dq:
            curr = []
            node = []
            for i in range(len(dq)):
                poped = dq.popleft()
                node.append(poped)
                curr.append(poped.val)
                if poped.left:
                    dq.append(poped.left)
                if poped.right:
                    dq.append(poped.right)
            if level % 2:
                for j in range(len(node)):
                    node[j].val = curr.pop()
            level += 1
        return root


        