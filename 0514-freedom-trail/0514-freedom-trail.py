class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(key)
        memo = {}
        #iterate trought keys left to right
        def dfs(r, k):
            if k >= n:
                return 0
            if (r, k) in memo:
                return memo[(r, k)]
            res = 1e7
            for i in range(len(ring)):
                if ring[i] == key[k]:
                    min_dist = min( abs(r-i), len(ring) - abs(r-i) )
                    res = min(res, 1 + min_dist + dfs(i, k+1))
            memo[(r, k)] = res 
            return res
        return dfs(0, 0)
            