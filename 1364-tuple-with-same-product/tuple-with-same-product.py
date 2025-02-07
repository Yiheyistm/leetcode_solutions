class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_map = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prdt = nums[i] * nums[j]
                my_map[prdt] += 1

        no_tuples = 0
        for values in my_map.values():
            if values > 1:
                no_tuples += (2*values) * (2*(values - 1))
        return no_tuples




        