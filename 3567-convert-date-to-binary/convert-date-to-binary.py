class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        res = []
        for d in date:
            res.append(str(bin(int(d))[2:]))
        return '-'.join(res)
        