class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx_sum = 0
        mn_sum = 0
        m_sum = 0
        r_sum = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            m_sum += nums[i]
            mx_sum = max(mx_sum, r_sum)
            mn_sum = min(mn_sum, m_sum)
            if r_sum < 0: r_sum = 0
            if m_sum > 0: m_sum = 0
        return mx_sum if mx_sum > -mn_sum else -mn_sum
        
        