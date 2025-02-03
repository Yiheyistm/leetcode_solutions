class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        result_list = []
        for i in range(len(ranges)):
            start, end = ranges[i]
            result_list.extend(range(start, end +1))

        st = set(result_list)
        for i in range(left, right +1):
            if i not in st:
                return False
     
        return True

    
        