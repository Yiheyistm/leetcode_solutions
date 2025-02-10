class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Selection sort
        for i in range(len(heights)):
            max_idx = i
            for j in range(i + 1, len(heights)):
                if heights[max_idx] <= heights[j]:
                     heights[j], heights[max_idx] = heights[max_idx], heights[j]
                     names[j], names[max_idx] = names[max_idx], names[j]
        return names
        