class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        uniques = sorted(cnt.keys())
        N = len(uniques)
        prev1, prev2 = 0, 0
        for i in range(N-1, -1, -1):
            earn = uniques[i] * cnt[uniques[i]]
            if  i + 1 < N and (uniques[i+1] - uniques[i] == 1):
                prev1, prev2 = max(earn + prev2, prev1), prev1
            else:
                prev1, prev2 = earn + prev1, prev1
        return prev1

           

        