class Solution {
public:
    int n;
    const int MOD = 1e9 + 7;
    vector<vector<vector<int>>> memo;

    int checkRecord(int n) {
        this->n = n;
        memo = vector<vector<vector<int>>>(
            n + 1, vector<vector<int>>(2, vector<int>(3, -1)));
        return dfs(0, 0, 0);
    }

    int dfs(int i, int totalAbsent, int consecLate) {
        if (i == n) {
            return 1;
        }

        if (memo[i][totalAbsent][consecLate] != -1) {
            return memo[i][totalAbsent][consecLate];
        }

        int res = dfs(i + 1, totalAbsent, 0) % MOD; // Append 'P'

        if (consecLate < 2) { // Append 'L'
            res = (res + dfs(i + 1, totalAbsent, consecLate + 1)) % MOD;
        }

        if (totalAbsent < 1) { // Append 'A'
            res = (res + dfs(i + 1, totalAbsent + 1, 0)) % MOD;
        }

        memo[i][totalAbsent][consecLate] = res;
        return res;
    }
};