class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = {}

        for i in range(len(paths)):
            new_pt = paths[i].split(' ')
            for j in range(1, len(new_pt)):
                s = new_pt[j].index('(')
                e = new_pt[j].index(')')
                key = new_pt[j][s + 1:e]
                path = new_pt[0] + "/" + new_pt[j][:new_pt[j].index('(')]
                # file_dict[new_pt[j][s + 1:e]] = new_pt[0] + "/" + new_pt[j][:new_pt[j].index('(')]
                if key in file_dict:
                    file_dict[key].append(path)
                else:
                    file_dict[key] = [path]
        fn = [ ]
        for v in file_dict.values():
            if len(v) > 1:
                fn.append(v)
        return fn

                
