class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = len(cardPoints) - k
        pfx = list(accumulate(cardPoints, initial = 0))

        ans = 0
        total = pfx[-1]
        for i in range(window, len(cardPoints) + 1):
            window_sum = pfx[i] - pfx[i - window]
            ans = max(ans, total - window_sum)
        return ans


        