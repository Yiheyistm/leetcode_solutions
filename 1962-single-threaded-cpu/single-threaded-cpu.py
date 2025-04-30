class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tsk = [ (e, p, i) for i, [e, p] in enumerate( tasks)]
        tsk.sort()

        time = tsk[0][0]
        heap = [(tsk[0][1], tsk[0][2])]
        res = []
        j = 1
        while heap:
            p, i = heappop(heap)
            res.append(i)
            time += p
            while j < len(tsk) and time >= tsk[j][0]:
                heappush(heap, (tsk[j][1], tsk[j][2]))
                j += 1
            if not heap and j < len(tsk) and time < tsk[j][0]:
                heappush(heap, (tsk[j][1], tsk[j][2]))
                time = tsk[j][0]
                j += 1
        return res


        

        