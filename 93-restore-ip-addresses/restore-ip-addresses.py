class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_Ip = []
        def creatValidIp(idx,dots, store):
            nonlocal valid_Ip
            if dots == 4 and idx == len(s):
                valid_Ip.append(store[:-1])
                return
            if dots > 4:
                return
            for j in range(idx, min(idx + 3, len(s))):
                nw = s[idx:j + 1]
                if int(nw) < 256 and (idx == j or s[idx] != '0'):
                    creatValidIp(j + 1, dots + 1, store + nw + '.')

        creatValidIp(0,0,'') 
        return valid_Ip
        
        