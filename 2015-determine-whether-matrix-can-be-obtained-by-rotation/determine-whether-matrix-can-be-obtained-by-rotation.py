class Solution:
    def show(self, res):
        for i in range(len(res)):
            print(res[i])
        print()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        result = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(4):
            for i in range(n):
                for j in range(n):
                    result[i][j] = mat[n-j -1][i]
            if result == target:
                return True
            mat = copy.deepcopy(result)
        return False

        