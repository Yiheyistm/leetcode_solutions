class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_pairs = {}
        no_pairs = 0
        for num in nums:
            if num in count_pairs:
                no_pairs += 1
                del count_pairs[num]
            else:
                count_pairs[num] = 1
        return [no_pairs, len(count_pairs)]

        