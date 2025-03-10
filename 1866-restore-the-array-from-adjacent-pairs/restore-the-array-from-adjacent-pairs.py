class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        for u,v in adjacentPairs:
                pairs[u].append(v)
                pairs[v].append(u)
        start = None
        for key, val in pairs.items():
            if len(val) == 1:
                start = key

        ans = [start]
        st = set()
        st.add(start)
        for _ in range(len(adjacentPairs)):
            val = pairs[ans[-1]]
            nxt = val[0] if val[0] not in st else val[1]
            st.add(nxt)
            ans.append(nxt)
        return ans
            



        