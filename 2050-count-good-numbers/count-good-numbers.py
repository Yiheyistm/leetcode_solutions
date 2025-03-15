class Solution:
    def countGoodNumbers(self, n: int) -> int:
        memo = defaultdict(int)
        MOD = 10**9 + 7
        def calc(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            ev1 = memo.get(n // 2) if  n // 2 in memo else calc(x, n // 2)
            memo[n // 2] = ev1
            ev2 = memo.get(n - n // 2) if  n - n // 2 in memo else calc(x, n - n // 2)
            memo[n - n // 2] = ev2
            return (ev1 * ev2) % MOD

        even = calc(5, n - n//2)
        memo = defaultdict(int) # reset the dictionary
        odd = calc(4, n //2)
        return (even * odd) % MOD