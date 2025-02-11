class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        max_h = 0
        print(citations)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                max_h = i + 1

        return max_h

        