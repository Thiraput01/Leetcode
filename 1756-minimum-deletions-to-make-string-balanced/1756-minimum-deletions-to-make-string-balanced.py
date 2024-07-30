class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        c = 0
        for i in s:
            if i == 'b':
                c += 1
            elif c:
                res +=1
                c -=1
        return res