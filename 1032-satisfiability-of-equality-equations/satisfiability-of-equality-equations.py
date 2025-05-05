class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i + 97):chr(i + 97) for i in range(26)}
        size = [1] * (26 + 1)
        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x
        def union(x,y):
            parX = find(x)
            parY = find(y)
            base = ord('a') - 1
            
            if parX != parY:
                sizeX = ord(parX) - base
                sizeY = sizeX = ord(parY) - base
                if size[sizeX] >= size[sizeY]:
                    parent[parY] = parX
                    size[sizeX] += size[sizeY]
                else:
                    parent[parX] = parY
                    size[sizeY] += size[sizeX]
        diff = []
        for eq in equations:
            if '!' in eq:
                diff.append(eq)
            else:
                union(eq[0], eq[-1])
    
        for eq in diff:
            if '!' in eq and find(eq[0]) == find(eq[-1]):
                return False
        return True
        