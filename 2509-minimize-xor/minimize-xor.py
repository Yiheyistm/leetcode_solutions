class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        max_limit = (10 ** 9).bit_length()
        
        ln2 = num2.bit_count()
        ans = [0] * (max_limit)

        while num1 and ln2:
            ln = num1.bit_length() - 1
            ans[ln] = 1
            ln2 -= 1
            num1 &= ~(1 << ln)

        for i in range(len(ans)):
            if ln2 == 0:
                break
            if ans[i] == 0:
                ans[i] = 1
                ln2 -= 1
        return int(''.join(map(str, ans[::-1])), 2)





