class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        lineS = [0] * (N + 1)
        for i in range(N):
            left = max(i - r, 0)
            right = min(N, i + r + 1)
            lineS[left] += stations[i]
            lineS[right] -= stations[i]

        def checker(mid):
            cur_k = k
            r_sum = 0
            cpy_line = lineS[:]
            for i in range(N):
                r_sum += cpy_line[i]
                if r_sum < mid:
                    needed = mid - r_sum
                    if needed > cur_k:
                        return False
                    cur_k -= needed
                    r_sum += needed
                    right = min(i + 2*r + 1, N)
                    cpy_line[right] -= needed
            return True

        low, high = min(stations), sum(stations) + k + 1
        while low + 1 < high:
            mid = (low + high) // 2
            if checker(mid):
                low = mid
            else:
                high = mid
        return low
        