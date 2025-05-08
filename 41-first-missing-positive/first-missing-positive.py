class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        heap = []
        freq = defaultdict(int)
        for num in nums:
            if num <= n and num > 0 and freq[num] == 0:
                heappush(heap, num)
                freq[num] += 1

        heap_len = len(heap)
        for i in range(1, heap_len + 1):
            if i != heappop(heap):
                return i
        return heap_len + 1
        

        