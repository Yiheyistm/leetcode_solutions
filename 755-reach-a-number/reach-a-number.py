class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)
        k = 0 
        while (k * (k + 1) / 2) < t or ((k * (k + 1) / 2) - t) % 2 == 1:
            k += 1
        return k