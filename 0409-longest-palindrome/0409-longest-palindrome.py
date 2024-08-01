class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        hasOne = False
        res = 0
        for k, v in m.items():
            if v % 2 == 0:
                res += v
            else:
                res += v-1
                hasOne = True
        res = res+1 if hasOne else res
        return res
