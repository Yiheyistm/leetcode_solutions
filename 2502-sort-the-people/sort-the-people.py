class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = sorted([(names[i], heights[i]) for i in range(len(names))], key = lambda x: -x[1])
        return [tuples[i][0] for i in range(len(names))]
        