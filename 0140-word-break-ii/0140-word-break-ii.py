class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return [""]

            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in word_set:
                    for sub_sentence in helper(j):
                        if sub_sentence:
                            res.append(word + " " + sub_sentence)
                        else:
                            res.append(word)
            memo[i] = res
            return res

        return helper(0)