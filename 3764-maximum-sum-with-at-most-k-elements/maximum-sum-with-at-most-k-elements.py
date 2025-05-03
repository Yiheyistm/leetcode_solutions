class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for r in range(len(grid)):
            temp = []
            for c in range(len(grid[0])):
                heappush(temp, grid[r][c])
                if len(temp) > limits[r]:
                    heappop(temp)
            heap.extend(temp)
            
        heapify(heap)
        while len(heap) > k:
            heappop(heap)
        return sum(heap)
        