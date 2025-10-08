class Solution:
    def nthUglyNumber(self, n: int) -> int:
            ugly = [1] #[1, 2, 3, 5, 6, 8, 9, 10, 12, 15, 18, .....]
            i2 = i3 = i5 = 0
            while len(ugly) < n:
                next2, next3, next5 = 2 * ugly[i2], 3 * ugly[i3],  5 * ugly[i5]
                next  = min(next2, next3, next5)
                ugly.append(next)
                if next == next2:
                    i2 += 1
                if next == next3:
                    i3 += 1
                if next == next5:
                    i5 += 1
                
            return ugly[-1]
        