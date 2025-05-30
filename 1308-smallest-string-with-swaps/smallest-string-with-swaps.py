class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        def union(x, y):
            parX = find(x)
            parY = find(y)
            if size[parX] >= size[parY]:
                parent[parY] = parX
                size[parX] += size[parY]
            else:
                parent[parX] = parY
                size[parY] += parX

        parent = [i for i in range(len(s))]
        size = [1] * len(s)

        for a, b in pairs:
            union(a, b)

        groups = defaultdict(list)
        for i in range(len(s)):
            root = find(i)
            heappush(groups[root], s[i])
        
        res = ''
        for i in range(len(s)):
            par = find(i)
            res += heappop(groups[par])
        return res

        


        