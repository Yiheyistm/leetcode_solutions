class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        groups = [phone_map[d] for d in digits]
        
        combos = product(*groups)
        
        return [''.join(letters) for letters in combos]

        