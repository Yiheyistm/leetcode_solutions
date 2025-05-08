class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(u, v):
            parU = find(u)
            parV = find(v)
            if parU != parV:
                
                valU = ord(parU)
                valV = ord(parV)
                if valU <= valV:
                    parent[parV] = parU
                elif valV < valU:
                    parent[parU] = parV

        parent = {chr(i + 97): chr(i + 97) for i in range(26)}
        for ch1, ch2 in zip(s1, s2):
            union(ch1, ch2)
        
        ans = ''
        for ch in baseStr:
            ans += find(ch)

        return ans
        