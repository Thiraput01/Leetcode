class Solution {
public:
    const int MOD = 1e9 + 7;

    int kInversePairs(int n, int k) {
        vector<vector<int>> dp(n+1, vector<int>(k+1, 0));

        // Base case: dp[i][0] = 1 for all i
        for (int i=1; i<=n; ++i) dp[i][0] = 1;
        

        for (int i=1; i<=n; ++i) {
            for (int j=1; j<=k; ++j) {
                for (int x=0; x <= min(j, i-1); ++x) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % MOD;
                }
            }
        }

        return dp[n][k];
    }
};
