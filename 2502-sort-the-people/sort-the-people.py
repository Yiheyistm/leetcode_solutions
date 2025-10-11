class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = {}
        for i in range(len(names)):
            tuples[heights[i]] = names[i]

        heights.sort(reverse = True)
        return [tuples[h] for h in heights]
        