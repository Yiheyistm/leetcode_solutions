class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            digits = list (str(nums[i]))
            sm = sum(map(int, digits))
            digit_sum[sm].append(i)
        
        max_sum = -1
        for val in digit_sum.values():
            if len(val) > 1:
                max_sum = max(max_sum, nums[val[-1]] + nums[val[-2]])
        return max_sum

                

        