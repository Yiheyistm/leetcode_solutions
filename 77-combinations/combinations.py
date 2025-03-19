class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        global_store = []
        def backtrack(idx, store):
            nonlocal n, k, global_store
            if len(store) == k:
                # print('YES')
                global_store.append(store[:])
                return

            for j in range(idx, n +1):
                store.append(j)
                backtrack(j+1, store)
                store.pop()
        backtrack(1, [])
        return global_store

        