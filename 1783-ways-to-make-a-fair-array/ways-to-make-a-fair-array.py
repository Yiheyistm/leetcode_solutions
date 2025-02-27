class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        tot_even = 0
        tot_odd = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                tot_even += nums[i]
            else:
                tot_odd += nums[i]
        
        cummulative_even_sum = 0
        cummulative_odd_sum = 0
        count = 0
        for i in range(len(nums)):
            tot_even -= nums[i] if i%2 == 0 else 0
            tot_odd -= nums[i] if i%2 != 0 else 0
            if tot_even + cummulative_odd_sum == tot_odd +cummulative_even_sum:
                count += 1
            cummulative_even_sum += nums[i] if i%2 == 0 else 0
            cummulative_odd_sum += nums[i] if i%2 != 0 else 0
        return count

        