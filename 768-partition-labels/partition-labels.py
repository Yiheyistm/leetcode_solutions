class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = defaultdict(int)
        for ch in s:
            my_dict[ch] = s.rindex(ch)

        ans = []
        mx_idx = 0
        idx = 0
        for i in range(len(s)):
            mx_idx = max(mx_idx, my_dict[s[i]])
            if i >= mx_idx:
                ans.append(mx_idx + 1 - idx)
                idx = mx_idx + 1

        return ans



        