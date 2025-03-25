class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_par = []
        def generate(store):
            if len(store) == 2 * n:
                check = []
                temp = store.copy()
                for ch in temp:
                    if ch == '(':
                        check.append(ch)
                    elif check  and check[-1] == '(' and ch == ')':
                        check.pop()
                    else: return

                if not check:
                    valid_par.append(''.join(store))
                return

            elif len(store) > 2 * n:
                return

            for b in ['(',')']:
                
                store.append(b)
                generate(store)
                store.pop()

        generate([])
        return valid_par




        