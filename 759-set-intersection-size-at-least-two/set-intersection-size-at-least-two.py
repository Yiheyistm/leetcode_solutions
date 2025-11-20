class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        prev1=intervals[0][1]-1
        prev2=intervals[0][1]
        c=2
        for i in range(1,n):
            if prev2<intervals[i][0]:
                prev1=intervals[i][1]-1
                prev2=intervals[i][1]
                c+=2
            elif prev1<intervals[i][0]:
                if intervals[i][1]==prev2:
                    prev1=intervals[i][1]-1
                else:
                    prev1=intervals[i][1]
                prev1,prev2=min(prev1,prev2),max(prev1,prev2)
                c+=1
        return c
        
        # intervals.sort(key=lambda item: (item[1], item[0]))
        # st = set()
        # ans = SortedSet([-inf])
        # for i in range(len(intervals)):
        #     if i in st: continue
        #     s, e = intervals[i]
        #     st.add(i)
        #     for j in range(i+1, len(intervals)):
        #         s1, e1  = intervals[j]
        #         if s1 < e:
        #             s = max(s, s1)
        #         elif s1 == e and not(s1 < ans[-1] < e1):
        #             ans.add(e1)
        #         elif s1 > e:
        #             break
        #         st.add(j)
        #     ans.add(s)
        #     ans.add(e)
        #     print(ans, st)
        # return len(ans) - 1
        