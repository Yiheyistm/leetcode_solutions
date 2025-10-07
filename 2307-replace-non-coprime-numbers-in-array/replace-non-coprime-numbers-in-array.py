class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and gcd(num, stack[-1]) > 1:
                pop = stack.pop()
                num = lcm(num, pop)
            stack.append(num)
        return stack

        