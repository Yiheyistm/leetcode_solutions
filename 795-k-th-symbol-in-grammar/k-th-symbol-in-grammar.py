class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n2 = n
        k2 = k
        path = [] # The path from last to parent
        while n2 > 0:
            path.append(k2)
            k2 = math.ceil(k2 / 2)
            n2 -= 1
        print(path)
        s = 0 # parent of all subsequence
        for i in range(len(path) -1, -1 ,-1):
            temp = []
            if s == 0:
                temp = [0,1]
            else:
                temp = [1,0]
            if path[i] % 2:
                s = temp[0]
            else:
                s = temp[1]
        return s