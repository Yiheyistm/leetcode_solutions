class Solution:
    def maskPII(self, s: str) -> str:
        # Email Address
        if '@' in s:
            s = s.lower()
            idx = s.index('@')
            s = s[0] + '*' * 5 + s[idx-1:]
            return s
        else:
            res = "".join(filter(str.isdigit, s))
            ctr_code = len(res) - 10
            
            res = '***-' * 2 + res[len(res) - 4:]
            if ctr_code == 0:
                return res
            return '+' + '*' * ctr_code + '-' + res
            

        