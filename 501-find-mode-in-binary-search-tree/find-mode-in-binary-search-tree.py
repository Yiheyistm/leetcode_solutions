# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def bst(node):
            if not node:
                return
            freq[node.val] += 1
            bst(node.left)
            bst(node.right)

        bst(root)
        mostFreq = dict(sorted(freq.items(), key = lambda item: item[1], reverse = True))
        _, fst_el = next(iter(mostFreq.items()))
        return [k  for k, val in mostFreq.items() if val == fst_el]
        