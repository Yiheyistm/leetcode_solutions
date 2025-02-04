from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lst = count.most_common(k)
        res = []
        for num in lst:
            key, _ = num
            res.append(key)
        return res
        