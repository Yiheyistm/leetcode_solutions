"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quadTree(r, c, size):
            val = grid[r][c]
            isSame = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        isSame = False
                        break
                if not isSame:
                    break
            if isSame:
                return Node(val == 1, True)
            
            mid = size // 2
            topLeft = quadTree(r, c, mid)
            topRight = quadTree(r, c + mid, mid)
            bottomLeft = quadTree(r + mid, c, mid)
            bottomRight = quadTree(r + mid, c + mid, mid)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        return quadTree(0,0, len(grid))



            
            


        