class Solution:
    def checkValidString(self, s: str) -> bool:
        lm, lM = 0, 0

        for i in s:
            if i == '(':
                lm += 1
                lM += 1
            elif i == ')':
                lm -= 1
                lM -= 1
            else:
                lm -= 1
                lM += 1
            if lM < 0:
                return False
            if lm < 0:
                lm = 0
        return lm == 0
        