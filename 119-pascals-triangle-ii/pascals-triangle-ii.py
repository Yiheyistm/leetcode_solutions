class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def triangle(s, rwIdx):
            if rwIdx == 0:
                return s
            
            nwArr = [1]
            for i in range(1,len(s)):
                nwArr.append(s[i] + s[i -1])
            nwArr.append(1)
            
            return triangle(nwArr, rwIdx - 1)

        return triangle([1], rowIndex)
        