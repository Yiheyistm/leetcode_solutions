class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        my_dict = {}
        for i in range(len(s)):
            my_dict[indices[i]] = s[i]
        s = ''
        for v in range(len(indices)):
            s += my_dict[v]
        return s