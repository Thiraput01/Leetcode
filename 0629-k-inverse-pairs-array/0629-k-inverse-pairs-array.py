class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1e9 + 7
        #   K 0 1 2
        # M 
        # 0   1 0 0
        # 1   1 0 0
        # 2   1 1 0
        # 3   1 2 2

        # dp[i][j] = [dp[i-1][j-k] for k in range(0, j)] 
        # **dont forgot case where j-k < 0 **
        # only need 2 row (i, i-1)
        
        prev = [0]*(k+1)
        prev[0] = 1

        for i in range(1, n+1):
            cur = [0]*(k+1)
            total = 0
            for j in range(0, k+1):

                if j >= i:
                    total -= prev[j-i]

                total = ( total + prev[j] ) % MOD
                cur[j] = total

            prev = cur

        return int(cur[k])
