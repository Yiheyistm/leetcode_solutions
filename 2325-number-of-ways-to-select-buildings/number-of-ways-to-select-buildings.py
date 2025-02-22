class Solution:
    def numberOfWays(self, s: str) -> int:
        cnt = Counter(s)
        cnt_0 = 0
        cnt_1 = 0
        count = 0
        for ch in s:
            if ch == '0':
                cnt_0 += 1
                cnt['0'] -= 1
                count += cnt_1 * cnt['1']
            else:
                cnt_1 += 1
                cnt['1'] -= 1
                count += cnt_0 * cnt['0']
        return count
        