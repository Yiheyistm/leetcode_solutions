class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j - 1]

        count = 0

        for y1 in range(cols):
            for y2 in range(y1, cols):
                prefix_sum_map = {0: 1}
                current_sum = 0
                
                for x in range(rows):
                    if y1 == 0:
                        row_sum = matrix[x][y2]
                    else:
                        row_sum = matrix[x][y2] - matrix[x][y1 - 1]
                    
                    current_sum += row_sum
                    
                    if (current_sum - target) in prefix_sum_map:
                        count += prefix_sum_map[current_sum - target]
                    
                    if current_sum in prefix_sum_map:
                        prefix_sum_map[current_sum] += 1
                    else:
                        prefix_sum_map[current_sum] = 1

        return count