class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        top = left = 0
        right = m - 1
        bottom = n - 1
        res = []
        while top <= bottom or left <= right:
            # TOP
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if bottom < top:
                break
            # RIGHT
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            # BOTTOM
            if right < left:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            # LEFT
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left:
                break
        return res
            


