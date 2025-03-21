class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(idx, store):
            nonlocal num
            if idx == len(num):
                for i in range(2, len(store)):
                    if store[i-1] + store[i-2] != store[i]:
                        return False
                return len(store) > 2
            
            for j in range(idx, len(num)):
                n = int(num[idx: j+1])
                if len(store) > 2 and store[-1] + store[-2] != n:
                    continue
                if len(str(n)) == len(num[idx: j+1]):
                    store.append(n)
                    if backtrack(j + 1, store):
                        return True
                    store.pop()
            return False

        return backtrack(0, [])
