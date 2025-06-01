class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        freq = cntr.most_common()[0][1]
        most_freq = set()
        for k, v in cntr.items():
            if v == freq:
                most_freq.add(k)

        min_len = float('inf')
        start_idx = {}
        for i,val in enumerate(nums):
            cntr[val] -= 1
            start_idx[val] = i if val not in start_idx else start_idx[val]
            if val in most_freq and cntr[val] == 0:
                min_len = min(min_len, i - start_idx[val] + 1)

        return min_len


        