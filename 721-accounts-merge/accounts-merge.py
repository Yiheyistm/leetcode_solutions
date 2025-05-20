class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        def union(x, y):
            parX = find(x)
            parY = find(y)
            if parX != parY:
                if size[parX] >= size[parY]:
                    parent[parY] = parX
                    size[parX] += size[parY]
                else:
                    parent[parX] = parY
                    size[parY] += size[parX]

        names = []
        email_dict = {}
        graph = []
        for i in range(len(accounts)):
            names.append(accounts[i][0])
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in email_dict:
                    graph.append((email_dict[accounts[i][j]], i))
                email_dict[accounts[i][j]] = i

        parent = {i:i for i in range(len(accounts))}
        size = [1] * len(accounts)
        for a, b in graph:
            union(a, b)
        
        email = [set() for _ in range(len(accounts))]
        for x in parent:
            p = find(x)
            email[p] |= set(accounts[x][1:])
        
        ans = []
        for i, em in enumerate(email):
            if em:
                temp = [names[i]]
                temp.extend(sorted(list(em)))
                ans.append(temp)
        return ans





            
        

        