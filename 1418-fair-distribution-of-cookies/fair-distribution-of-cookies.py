class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn = float('inf')
        def backtrack(idx, store):
            nonlocal cookies, k,mn
            if idx == len(cookies):
                mx = max(store)
                mn = min(mn, mx)
                return
            for j in range(k):
                c = store[j] + cookies[idx]
                if c > mn: continue
                store[j] = c
                backtrack(idx+1, store)
                store[j] -= cookies[idx]
        backtrack(0, [0] * k)
        return mn
        