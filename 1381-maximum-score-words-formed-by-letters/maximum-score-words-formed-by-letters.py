class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def canform(word, l_count):
            temp = l_count.copy()
            for ch in word:
                if temp[ch] == 0:
                    return False
                temp[ch] -= 1
            return True

        def wordForm(idx, curr_score, l_count):
            nonlocal max_score
            max_score = max(max_score, curr_score)

            for i in range(idx, len(words)):
                word = words[i]
                if canform(word, l_count):  
                    word_score = sum(score_dict[ch] for ch in word)
                    for ch in word:
                        l_count[ch] -= 1
                    
                    wordForm(i + 1, curr_score + word_score, l_count)

                    for ch in word:
                        l_count[ch] += 1


        cnt = Counter(letters)
        score_dict = {}
        max_score = 0
        for i in range(len(score)):
            ch = chr(i + ord('a'))
            score_dict[ch] = score[i]

        wordForm(0,0, cnt)
        return max_score


        