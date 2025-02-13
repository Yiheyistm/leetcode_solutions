class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        win_sum = 0
        for i in range(k):
            win_sum += nums[i]
        left = 0
        max_sum = win_sum
        for right in range(k,len(nums)):
            win_sum -= nums[left]   
            win_sum += nums[right]
            max_sum = max(max_sum, win_sum)
            left += 1
        return max_sum / k

        