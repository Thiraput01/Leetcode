class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def isPal(st, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(i, total):
            if i == n:
                res.append(total)
                return

            #check palindrome
            for j in range(i, n):
                if isPal(s, i, j):
                    dfs(j+1, total + [s[i:j+1]])
        
        dfs(0, [])
        return res
