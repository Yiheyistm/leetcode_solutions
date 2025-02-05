class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = inf
        ls_dict = {}
        for i, ch in enumerate(list1):
            ls_dict[ch] = i

        for i, ch in enumerate(list2):
            if ch in ls_dict:
                min_sum = min(min_sum, ls_dict[ch] + i)
                ls_dict[ch] += i
        res = []
        for key in ls_dict:
            if ls_dict[key] == min_sum and key in list2:
                res.append(key)
        return res
        