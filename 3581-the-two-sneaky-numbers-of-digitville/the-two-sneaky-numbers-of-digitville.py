class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        res = []
        for key, value in num_dict.items():
            if value > 1:
                res.append(key)
        return res

        