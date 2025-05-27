class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]

        def union(x, y):
            parX = find(x)
            parY = find(y)
            if parX != parY:
                if size[parX] >= size[parY]:
                    parent[parY] = parX
                    size[parX] += size[parY]
                else:
                    parent[parX] = parY
                    size[parY] += size[parX]
        n = len(source)
        parent = [ i for i in range(n) ]
        size = [1] * n
                
        for a, b in allowedSwaps:
            union(a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)

        dist = 0
        for idxs in groups.values():
            source_cnt = Counter(source[i] for i in idxs)
            target_cnt = Counter(target[i] for i in idxs)
            for val in target_cnt:
                matched = min(target_cnt[val], source_cnt.get(val, 0))
                dist += target_cnt[val] - matched

        return dist
