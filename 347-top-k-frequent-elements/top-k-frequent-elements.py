from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num, cnt in freq.items():
            heappush(heap, (cnt, num))
            if len(heap) > k:
                heappop(heap)
        return [num for cnt, num in heap]
        