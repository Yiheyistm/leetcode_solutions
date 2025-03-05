class Solution:
    def numberOfSteps(self, num: int) -> int:
        cn = 0
        while num:
            q, r = divmod(num, 2)
            num = q
            if not num: cn += 1;break
            cn += 1 + r
        return cn
        