class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        curr_max = 1
        for i in range(n):
            #odd length
            l, r = i, i
            while l>=0 and r<=n-1 and s[l] == s[r]:
                if r-l+1 > curr_max:
                    curr_max = r-l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
            #even length
            l, r = i, i+1
            while l>=0 and r<=n-1 and s[l] == s[r]:
                if r-l+1 > curr_max:
                    curr_max = r-l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
        return ans if curr_max != 1 else s[0]