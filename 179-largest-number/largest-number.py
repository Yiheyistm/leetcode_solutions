from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)
        nums = sorted(nums, key = cmp_to_key(lambda x, y: -1 if x + y < y + x else 1), reverse = True)
       
        return ''.join(nums) if nums[0] != '0' else '0'

        
        