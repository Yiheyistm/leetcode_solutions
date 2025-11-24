class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        res = []
        for bit in nums:
            num =(num * 2) + bit
            if num % 5 == 0:
                res.append(True)
            else: res.append(False)
        return res