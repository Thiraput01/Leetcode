class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        a_count_right = 0
        for i in s:
            if i=='b':
                a_count_right += 1
            elif a_count_right:
                res +=1
                a_count_right -=1
        return res