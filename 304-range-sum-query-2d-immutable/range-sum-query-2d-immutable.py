class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.mat = [[0] * (cols +1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.mat[i][j] = self.mat[i][j - 1] + self.mat[i - 1][j] \
                - self.mat[i - 1][j - 1] + matrix[i - 1][j - 1]
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.mat[r2 + 1][c2 + 1] - self.mat[r2 + 1][c1] \
         - self.mat[r1][c2 + 1] + self.mat[r1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)