class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        answer = []
        np = len(pattern)
        for query in queries:
            p = 0
            s = 0
            nq = len(query)
            st = ''
            while s < nq:
                if p < np and query[s] == pattern[p]:
                    p += 1
                    st += query[s]
                elif query[s].isupper():
                    st += query[s]
                s += 1
            answer.append(st == pattern)
               
        return answer

            