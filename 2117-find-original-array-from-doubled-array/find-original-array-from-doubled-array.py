class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        count = {}
        for num in changed:
            count[num] = count.get(num, 0) + 1

        changed.sort()
        res = []
        for num in changed:
            if count.get(num, 0) == 0:
                continue
            elif count.get(2 * num, 0) == 0:
                return []
            res.append(num)
            count[num] -= 1
            count[2 * num] -= 1
        return res