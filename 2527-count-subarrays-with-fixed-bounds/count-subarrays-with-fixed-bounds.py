class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_pos = max_pos = left = -1 
        res = 0  

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left = i  
                min_pos = max_pos = -1
            
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            
            if min_pos != -1 and max_pos != -1:
                res += max(0, min(min_pos, max_pos) - left)
        return res
