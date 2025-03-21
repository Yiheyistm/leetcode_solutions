class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        mn = float('inf')
        def backtrack(idx, store, curr_max):
            nonlocal jobs, k,mn
            if idx == len(jobs):
                mn = min(mn, curr_max)
                return
            for j in range(k):
                if store[j] + jobs[idx] > mn: continue
                store[j] += jobs[idx]
                backtrack(idx+1, store, max(curr_max, store[j]))
                store[j] -= jobs[idx]
                if store[j] == 0:
                    break
        backtrack(0, [0] * k, 0)
        return mn
        