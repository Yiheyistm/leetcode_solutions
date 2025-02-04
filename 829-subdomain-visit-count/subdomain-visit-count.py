class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited_dict = {}
        for web in cpdomains: 
            no, link = web.split(' ')
            i = 0
            for _ in range(link.count('.') + 1):
                key = link
                visited_dict[key] = visited_dict.get(key, 0) + int(no)
                idx = link.find('.')
                link = link[idx+1:]
               
        res = []
        for key, value in visited_dict.items():
            res.append(f"{value} {key}") 
        
        print(res)
        return res




        