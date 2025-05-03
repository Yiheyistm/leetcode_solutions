class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for r in range(len(grid)):
            for num in sorted(grid[r], reverse = True)[:limits[r]]:
                heappush(heap, num)
                if len(heap) > k:
                    heappop(heap)
        return sum(heap)
        