class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited_dict = {}
        for web in cpdomains: 
            no, link = web.split(' ')
            for _ in range(link.count('.') + 1):
                visited_dict[link] = visited_dict.get(link, 0) + int(no)
                idx = link.find('.')
                link = link[idx+1:]
               
        res = []
        for key, value in visited_dict.items():
            res.append(f"{value} {key}") 
        return res




        