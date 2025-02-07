class Solution:
    def move_diagonal(self, mat, a ,b, dir):
        ls = []
        i , j = a, b
        if dir == 'bltr':
            while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                ls.append(mat[i][j])
                i -= 1
                j += 1
        else:
            while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                ls.append(mat[i][j])
                i += 1
                j -= 1
        idx = (i+1, j) if dir == 'bltr' else (i, j+1)
        return ls, idx


    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        res = []
        i = j = 0
        while i < n and j < m:
            if (i + j) % 2 == 0:
                lst, idx = self.move_diagonal(mat,i,j,'bltr')
                res.extend(lst)
                if idx[1] >= m:
                    i = idx[0] + 1
                    j = idx[1] - 1
                else:
                    i = idx[0]
                    j = idx[1]
            else:
                lst, idx = self.move_diagonal(mat,i,j,'trbl')
                res.extend(lst)
                if idx[0] >= n:
                    i = idx[0]-1
                    j = idx[1]+ 1
                else:
                    i = idx[0]
                    j = idx[1]
        return res


        