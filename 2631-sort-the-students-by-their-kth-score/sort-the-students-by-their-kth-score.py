class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        matrix_map = defaultdict(list)
        for i in range(len(score)):
            matrix_map[score[i][k]] = score[i]

        key_list = list(matrix_map.keys())
        key_list.sort(reverse = True)
        score = []
        for k in key_list:
            score.append(matrix_map[k])
        del matrix_map
        del key_list
        return score
        
        