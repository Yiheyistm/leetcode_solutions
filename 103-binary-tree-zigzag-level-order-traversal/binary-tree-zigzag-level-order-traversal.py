# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node, level, stack):
            if not node:
                return []

            if len(stack) <= level:
                stack.append(deque())
            if level % 2:
                stack[level].appendleft(node.val)
            else:
                stack[level].append(node.val)
            bfs(node.left, level + 1, stack)
            bfs(node.right, level + 1, stack)
            return stack
        dq = bfs(root, 0, [])
        return [list(child) for child in dq]
        