class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        M = 10 ** 9 + 7

        powers = []
        i = 1
        while True:
            power_val = i ** x
            if power_val > n:
                break
            powers.append(power_val)
            i += 1

        N = len(powers)
        store = [[-1] * (n + 1) for _ in range(N + 1)]
        print(powers)
        def dp(i , rem):
            if rem == 0: return 1
            if i == N or rem < 0: return 0

            if store[i][rem] == -1:
                skip = dp(i + 1, rem)
                take = dp(i + 1, rem - powers[i])
                store[i][rem] = (skip + take) % M
            return store[i][rem]  
        return dp(0, n)
       

        