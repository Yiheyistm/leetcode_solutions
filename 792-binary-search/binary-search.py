class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec(l, r):
            nonlocal target, nums
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if l >= r:
                return -1
            if target > nums[mid]:
               return rec(mid + 1, r)
            else: 
                return rec(l, mid - 1)
                
        return rec(0, len(nums) -1)
        
        

        