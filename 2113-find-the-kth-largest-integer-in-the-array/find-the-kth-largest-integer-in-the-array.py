class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if len(nums) == 0 or k > len(nums):
           return "" 
        nums.sort(key= lambda x: int(x))
        return nums[-k]
        