class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        uniques = sorted(cnt.keys())
        N = len(uniques)
        points = []
        for i in range(N):
            points.append(uniques[i] * cnt[uniques[i]])


        prev1, prev2 = points[0], 0
        for i in range(1, N):
            if (uniques[i] - uniques[i-1] == 1):
                prev1, prev2 = max(points[i] + prev2, prev1), prev1
            else:
                prev1, prev2 = points[i] + prev1, prev1
        return prev1

           

        