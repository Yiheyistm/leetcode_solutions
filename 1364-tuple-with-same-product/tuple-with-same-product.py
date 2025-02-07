class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_map = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prdt = nums[i] * nums[j]
                my_map[prdt].append([i,j])

        no_tuples = 0
        for values in my_map.values():
            n = len(values)
            if n > 1:
                no_tuples += (2*n) * (2*(n - 1))
        return no_tuples




        