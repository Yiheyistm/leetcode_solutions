class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",          
            
        }
        res = []
        ans = ''
        for key, value in num_map.items():
            while num >= key:
                print('4' == str(num)[0])
                if '4' == str(num)[0]:
                    mx = min(k for k in num_map if k >= num)
                    ans += num_map[key] + num_map[mx]
                    dif = 4 * key
                    num -= dif
                    print(ans, mx,dif, num)
                elif '9' == str(num)[0]:
                    mn = min(k for k in num_map if k <= num and len(str(k)) == len(str(num)))
                    mx = min(k for k in num_map if k >= num)
                    ans += num_map[mn] + num_map[mx]
                    dif = 9 * mn
                    num -= dif
                    print(ans, mx,dif, num)
                    
                else:
                    ans += num_map[key]
                    num -= key
                    print(ans, num)
        return ans






        # st = str(num)
        # for i in range(len(st)):
        #     if st[i] != '0':
        #         res.append(st[i] + '0' * (len(st) - i - 1))
        #     else:
        #         res.append(st[0])
        # ans = ''
        # for i in range(len(res)):
        #     mx = max(k for k in num_map if k <= int(res[i]))
        #     if res[i][0] == '4':
        #         mn = min(k for k in num_map if k >= int(res[i]))
        #         ans += num_map[mx] + num_map[mn]
        #         print(res[i],mn, mx, ans)

        #     elif 10**(len(res[i])-1) == mx:
        #             ans += num_map[mx] * (len(res[i]) - 1)
                    
        #     else:
        #         if int(res[i]) % mx == 0:
        #             ans += num_map[mx]
        #         else:
        #             diff = int(res[i])- mx
        #             mx2 = max(k for k in num_map if k <= diff)
        #             ans += num_map[mx] + num_map[mx2] * (diff // mx2)
            
        #     print(ans)




        