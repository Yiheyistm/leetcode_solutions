class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        def calc(dp, start, end):
            for i in range(start, end + 1):
                dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
            return dp[-1]

        dp1 = [0] * (len(nums) -1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2 = [0] * (len(nums))
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])


        first =  calc(dp1, 2, len(nums)-2)
        sec =  calc(dp2,3, len(nums)-1)
        return max(first, sec)

        