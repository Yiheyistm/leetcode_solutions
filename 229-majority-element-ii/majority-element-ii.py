class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dup_dict = {}
        min = len(nums) // 3
        res = []
        for num in nums: 
            dup_dict[num] = dup_dict.get(num, 0) + 1
            if dup_dict[num] > min and num not in res:
             res.append(num)
        return res
        