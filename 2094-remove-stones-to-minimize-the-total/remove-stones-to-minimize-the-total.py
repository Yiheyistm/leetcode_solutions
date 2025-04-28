class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        num = []
        for val in piles:
            heappush(num, -val)
        for _ in range(k):
            val = -heappop(num)
            heappush(num, -(val - (val // 2)))
        return -sum(num)
        