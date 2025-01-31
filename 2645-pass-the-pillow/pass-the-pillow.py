class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 0 # 0 for right direction and 1 for left direction
        i = 1
        count = 0
        while i <= n:
            if count == time:
                break
            if i == n:
                direction = 1
            if i == 1:
                direction = 0
            if direction == 0:
                i += 1
            if direction == 1:
                i -= 1
            count += 1
        return i

        