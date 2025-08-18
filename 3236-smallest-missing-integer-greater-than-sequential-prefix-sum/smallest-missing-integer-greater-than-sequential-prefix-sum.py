class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        r_sum = 0
        for r, num in enumerate(nums):
            if r == 0:  r_sum += num
            elif nums[r -1] + 1 == num: r_sum += num
            else: break
    
        while True:
            if r_sum not in nums:break
            r_sum += 1
        return r_sum
                    

        