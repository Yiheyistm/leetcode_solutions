class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        max_h = 0
        for i in range(n):
            curr = n - i
            if citations[i] >= curr:
                max_h = max(max_h, curr)

        return max_h

        