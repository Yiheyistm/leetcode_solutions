class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mncost = 0
        nums = [instructions[0]]
        for i in range(1, len(instructions)):
            idx = bisect_left(nums, instructions[i])
            idx2 = bisect_right(nums, instructions[i])
            mncost = (mncost +  min(idx, i - idx2)) % MOD
            if idx == len(nums):
                nums.append(instructions[i])
            else:
                nums.insert(idx, instructions[i])
        return mncost
            

        