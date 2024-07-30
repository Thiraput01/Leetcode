class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = len(s3)
        
        if n + m != l:
            return False
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        
        for i1 in range(n, -1, -1):
            for i2 in range(m, -1, -1):
                if i1 < n and s1[i1] == s3[i1 + i2] and dp[i1 + 1][i2]:
                    dp[i1][i2] = True
                if i2 < m and s2[i2] == s3[i1 + i2] and dp[i1][i2 + 1]:
                    dp[i1][i2] = True
        
        return dp[0][0]
