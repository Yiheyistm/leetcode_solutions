class Solution:
    def simplifyPath(self, path: str) -> str:
        pthStack = []
        pth = [part for part in path.split("/") if part]
        for ch in pth:
            if ch == '.': continue
            elif ch == '..':
                if pthStack:
                    pthStack.pop()
            else:
                pthStack.append(ch)
        return '/' + '/'.join(pthStack)


        