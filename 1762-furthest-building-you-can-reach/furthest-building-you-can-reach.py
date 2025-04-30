class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []
        for i in range(len(heights) - 1):
            jump =  heights[i + 1] - heights[i]
            if len(heap) < ladders and jump > 0:
                heappush(heap, jump)
            elif len(heap) == ladders and jump > 0:
                heappush(heap, jump)
                j = heappop(heap)
                if j <= bricks:
                    bricks -= j
                else:
                    return i
        return len(heights) - 1
  

        