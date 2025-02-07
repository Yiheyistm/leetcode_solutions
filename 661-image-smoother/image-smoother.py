class Solution:
    def get_avg(self, matrix, i, j) -> int:
        sum = matrix[i][j]
        count = 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),    (0, 1),
            (1, -1),  (1, 0),  (1, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                sum += matrix[ni][nj]
                count += 1
        return sum // count

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        result = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                avg = self.get_avg(img, i, j)
                result[i][j] = avg
        return result
        


        