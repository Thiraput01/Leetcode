class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7;
        cache = {}
        
        def dfs(cR, cC, cM):
            if(cM > maxMove):
                return 0
            if(cR >= m or cR < 0 or
               cC >= n or cC < 0):
                return 1;
            if((cR, cC, cM) in cache):
                return cache[(cR, cC, cM)]
            l = dfs(cR, cC-1, cM+1)
            r = dfs(cR, cC+1, cM+1)
            u = dfs(cR-1, cC, cM+1)
            d = dfs(cR+1, cC, cM+1)
            cache[(cR, cC, cM)] = (l + r + u + d) % MOD
            return cache[(cR, cC, cM)]
        
        return dfs(startRow, startColumn, 0)