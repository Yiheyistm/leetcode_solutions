class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        res = []
        for bit in nums:
            num =(num * 2) + bit
            res.append(num % 5 == 0)
        return res