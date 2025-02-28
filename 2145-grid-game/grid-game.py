class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        frs = []
        srs = []
        fac = 0
        sac = 0
        for f, s in zip(grid[0], grid[1]):
            fac += f 
            sac += s
            frs.append(fac - grid[0][0]) # we have to exclude the initial value because it is the start point of the red robot 
            srs.append(sac)

        srs[-1] -= grid[1][len(grid[0]) - 1]  # since it is the end point of the red robot it has to be decrease from the blue robot possible cells
        c = 0
        while c < len(grid[0]) - 1:
            d1 = max(frs[-1] - frs[c + 1], srs[c])
            d2 = max(frs[-1] - frs[c], srs[c - 1] if c > 0 else 0)
            if d1 < d2:
                c+=1
            else:
                return d2

        return srs[-1]


        