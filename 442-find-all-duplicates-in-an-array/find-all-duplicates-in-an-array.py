from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        double_dict = Counter(nums)
        res = []
        for k in double_dict:
            if double_dict[k] > 1:
                res.append(k)
        return res