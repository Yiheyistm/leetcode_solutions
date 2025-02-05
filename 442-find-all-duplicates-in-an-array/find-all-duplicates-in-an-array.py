class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        double_dict = {}
        for num in nums:
            double_dict[num] = double_dict.get(num, 0) + 1
        res = []
        for k in double_dict:
            if double_dict[k] > 1:
                res.append(k)
        return res