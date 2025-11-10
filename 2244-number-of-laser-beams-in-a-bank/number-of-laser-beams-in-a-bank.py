class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = None
        res = 0
        for row in bank:
            one_count = row.count('1')
            if one_count and prev:
                res += one_count * prev
            if one_count:
                prev = one_count
        return res