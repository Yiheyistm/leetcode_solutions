class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i,j = len(a)-1, len(b) -1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            bit1 = a[i] if i >= 0 else '0'
            bit2 = b[j] if j >= 0 else '0'
            if bit1 == '1' and bit2 == '1':
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
                    carry = 1
            elif bit1 == '1' or bit2 == '1':
                if carry:
                    res = '0' + res
                    carry = 1
                else:
                    res = '1' + res
            else:
                if carry:
                    res = '1' + res
                    carry = 0
                else:
                    res = '0' + res
            i -= 1
            j -= 1
        return res
            
        