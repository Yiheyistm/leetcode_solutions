class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[ 0 for _ in range(n - 2)] for _ in range(n - 2)]
        print(maxLocal)
        i = j = 0
        i_count = 0
        while i < n - 2:
            md_i = i + 1
            md_j = j + 1
            mx = 0
            for k in range(md_i - 1, md_i - 1 + 3):
                for l in range(md_j - 1, md_j - 1 + 3):
                    mx = max(mx, grid[k][l])
            maxLocal[i][j] = mx
            i_count += 1
            j += 1
            if i_count == n - 2:
                i += 1
                j = 0
                i_count = 0
        return maxLocal
        