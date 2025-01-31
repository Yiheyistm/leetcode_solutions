class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        res = []
        n = len(nums)
        for i, num in enumerate(nums):
            # when numbers[i] == 0
            if num == 0:
                res.append(num)
            # when numbers[i] > 0 and  when numbers[i] < 0
            else:
                print(num)
                r = (num + i) % n
                print(r)
                res.append(nums[r])
        return res
        