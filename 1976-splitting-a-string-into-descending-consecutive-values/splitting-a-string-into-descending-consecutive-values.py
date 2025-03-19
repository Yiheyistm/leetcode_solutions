class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, store):
            nonlocal s

            if i == len(s):
                for j in range(1, len(store)):
                    if store[j -1] - store[j] != 1:
                        return False
                return len(store) > 1

            for j in range(i, len(s)):
                num = int(s[i: j+ 1])
                if store and store[-1] - num != 1: continue
                store.append(num)
                if backtrack(j + 1, store):
                    return True
                store.pop()
            return False
        return backtrack(0, [])
        