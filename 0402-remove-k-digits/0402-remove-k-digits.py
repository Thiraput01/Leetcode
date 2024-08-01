class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for c in num:
            while k > 0 and s and s[-1] > c:
                s.pop()
                k -= 1
            if not s and c == '0':
                continue
            s.append(c)
        ans = "".join(s)
        if k > 0:
            ans = ans[:len(s)-k]
        return ans if ans else '0'
            