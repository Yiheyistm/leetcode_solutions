class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        merges = list(zip(nums, cost))
        merges.sort()
        cm_cost = 0
        pfx_sum = [0] * len(nums)
        for i in range(1, len(merges)):
            cm_cost += merges[i -1][1]
            pfx_sum[i] = (pfx_sum[i-1] + ((merges[i][0] - merges[i -1][0]) * cm_cost))

        cm_cost = 0
        sfx_sum = [0] * len(nums)
        for i in range(len(merges) - 2, -1, -1):
            cm_cost += merges[i + 1][1]
            sfx_sum[i] = (sfx_sum[i + 1] + (abs(merges[i][0] - merges[i + 1][0]) * cm_cost))

        min_cost = float('inf')
        for pfx, sfx in zip(pfx_sum, sfx_sum):
            min_cost = min(min_cost, pfx + sfx)
        return min_cost

        





        
        