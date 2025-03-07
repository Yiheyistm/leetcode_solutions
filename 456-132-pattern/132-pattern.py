class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        decStk = []
        third = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third: 
                return True
            while decStk and decStk[-1] < nums[i]:
                third = decStk.pop()
            decStk.append(nums[i])

        return False
        