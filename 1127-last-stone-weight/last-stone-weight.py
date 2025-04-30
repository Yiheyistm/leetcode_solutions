class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for st in stones:
            heappush(heap, -st)
        
        while len(heap) > 1:
            y, x = -heappop(heap), -heappop(heap)
            if y > x:
                heappush(heap, x - y)
        return -heap[0] if heap else 0
        