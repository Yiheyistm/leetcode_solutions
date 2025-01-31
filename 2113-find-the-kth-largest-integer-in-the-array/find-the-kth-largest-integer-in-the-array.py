class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if len(nums) == 0 or k > len(nums):
           return "" 
        my_list = list(map(int, nums))
        my_list.sort()
        return str(my_list[-k])
        