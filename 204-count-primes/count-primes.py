class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
        
        count = 0
        for i in range(n):
            if is_prime[i]:
                count += 1
        
        return count