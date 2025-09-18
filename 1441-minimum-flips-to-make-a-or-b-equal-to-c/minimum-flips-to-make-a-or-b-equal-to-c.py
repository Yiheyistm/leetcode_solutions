class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        xor_ = (a | b) ^ c
        and_ = (a & b)
        cnt = 0
        k = 0
        while xor_:
            if xor_ & 1:
                if (1 << k) & and_:
                    cnt += 2
                else:
                    cnt += 1
            xor_ >>= 1
            k += 1
        
        return cnt


                                                                                            