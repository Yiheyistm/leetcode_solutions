class Solution:
    def countGoodNumbers(self, n: int) -> int:
        memo = defaultdict(int)
        memo2 = defaultdict(int)
        MOD = 10**9 + 7
        def calc5(n):
            if n == 0:
                return 1
            if n == 1:
                return 5
            ev1 = memo.get(n // 2) if  n // 2 in memo else calc5(n // 2)
            memo[n // 2] = ev1
            ev2 = memo.get(n - n // 2) if  n - n // 2 in memo else calc5(n - n // 2)
            memo[n - n // 2] = ev2
            return (ev1 * ev2) % MOD
        
        def calc4(n):
            if n == 0:
                return 1
            if n == 1:
                return 4
            ev1 = memo2.get(n // 2) if  n // 2 in memo2 else calc4(n // 2)
            memo2[n // 2] = ev1
            ev2 = memo2.get(n - n // 2) if  n - n // 2 in memo2 else calc4(n - n // 2)
            memo2[n - n // 2] = ev2
            return (ev1 * ev2) % MOD
        return (calc5(n - n//2) * calc4(n//2)) % MOD