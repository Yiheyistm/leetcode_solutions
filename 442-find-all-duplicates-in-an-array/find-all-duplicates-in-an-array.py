class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = set()
        n = len(nums)
        no_dup = 0
        while i < n - no_dup:
            correct_pos = nums[i] -1
            if correct_pos == i:
                i += 1
            else:
                
                if nums[i] == nums[correct_pos]:
                    res.add(nums[i])
                    no_dup += 1
                    nums[i], nums[-no_dup] = nums[-no_dup], nums[i]
                else:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
        return list(res)
            
        