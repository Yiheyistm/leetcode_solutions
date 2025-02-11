class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num2 = sorted(nums, reverse = True)
        freq_map = {}
        for i, num in enumerate(num2):
            if num in freq_map:
                freq_map[num] -= 1
            else:
                freq_map[num] = freq_map.get(num, 0) + len(nums) - 1- i

        for i in range(len(nums)):
            nums[i] = freq_map[nums[i]]
        return nums
                
        
        