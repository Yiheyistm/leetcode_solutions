class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        col_map = {}
        for i, row in enumerate(score):
            col_map[row[k]] = i
        return [score[col_map[i]] for i in sorted(col_map.keys(), reverse= True)]

        