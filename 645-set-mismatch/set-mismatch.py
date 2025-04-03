class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = OrderedDict()
        n = len(nums)
        while i < n:
            correct_pos = nums[i] -1
            if nums[i] in res and nums[correct_pos] != nums[i]:
                res.pop(nums[i])
                res[i + 1] = 1
            if correct_pos == i:
                i += 1
            else:
                
                if nums[i] == nums[correct_pos]:
                    res[nums[i]] = 1
                    res[(i + 1)] = 1
                    i += 1
                else:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
        return list(res.keys())
            
        
        