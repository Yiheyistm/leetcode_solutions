class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        flag = False #for block comments
        st = '' # strings that are added to the result
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                # before the line encounter start of block comment
                if not flag:
                    # start of block comment
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        flag = True
                        i += 2
                        continue
                    # start of single line comments
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        st += line[i]
                        i += 1
                # after finding start commnet 
                else:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        flag = False
                        i += 2
                    else:
                        i += 1
            if not flag and st:
                res.append(st)
                st = ''
        return res

                

                    
 
                

        