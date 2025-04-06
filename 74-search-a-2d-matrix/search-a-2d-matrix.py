class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix); m = len(matrix[0])
        l = 0; r = (n * m) - 1
        while l <= r:
            mid = (l + r) // 2
            rw = (mid) // m
            cl = (mid) % m
            print(rw, cl, mid)
            val = matrix[rw][cl]
            if val == target:
                return True
            elif val < target: l = mid + 1
            else: r = mid - 1
        return False


        