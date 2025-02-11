class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles) - 2
        sum = 0
        while i < j:
            sum += piles[j]
            j -= 2
            i += 1
        return sum
