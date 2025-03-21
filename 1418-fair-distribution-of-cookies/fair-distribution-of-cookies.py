class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn = float('inf')
        def backtrack(idx, store, curr_max):
            nonlocal cookies, k,mn
            if idx == len(cookies):
                mn = min(mn, curr_max)
                return
            for j in range(k):
                if store[j] + cookies[idx] > mn: continue
                store[j] += cookies[idx]
                backtrack(idx+1, store, max(curr_max, store[j]))
                store[j] -= cookies[idx]
                if store[j] == 0:
                    break
        backtrack(0, [0] * k, 0)
        return mn
        