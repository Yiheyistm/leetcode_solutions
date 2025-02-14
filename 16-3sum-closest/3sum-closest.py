class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        max_sum = float('-inf')
        dist = float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                sm = nums[l] + nums[r] + nums[i]
                d = abs(sm - target)
                if d < dist:
                    dist = d
                    max_sum = sm
                elif d == dist:
                    max_sum = max(max_sum, sm)
                if sm == target:
                    l += 1
                    r -= 1
                elif sm < target:
                    l += 1
                else:
                    r -= 1

        return max_sum
        