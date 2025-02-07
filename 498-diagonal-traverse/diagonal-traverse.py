class Solution:
    def move_diagonal(self, mat, i ,j, dir):
        ls = []
        while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
            ls.append(mat[i][j])
            if dir == 'bltr':
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
               
        idx = (i+1, j) if dir == 'bltr' else (i, j+1)
        return ls, idx


    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        i = j = 0
        while i < len(mat) and j < len(mat[0]):
            if (i + j) % 2 == 0:
                lst, (i, j) = self.move_diagonal(mat,i,j,'bltr')
                res.extend(lst)
                if j >= len(mat[0]):
                    i +=  1
                    j -=  1
            else:
                lst, (i, j) = self.move_diagonal(mat,i,j,'trbl')
                res.extend(lst)
                if i >= len(mat):
                    i -= 1
                    j += 1
        return res


        