class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        for num in arr:
            cnt[num % k] += 1
        print(dict(cnt))
        for i in cnt.keys():
            l = k - i
            if i != 0 and (l not in cnt or cnt[l] != cnt[i] or (l == i and cnt[l] % 2 == 1)):
                return False
        return True

        