class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for ch in strs:
            key = ''.join(sorted(ch))
            if key in my_dict:
                my_dict[key].append(ch)
            else:
                my_dict[key] = [ch]
        ans = []
        for val in my_dict.values():
            ans.append(val)
        return ans
        