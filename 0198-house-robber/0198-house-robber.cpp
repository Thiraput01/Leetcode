class Solution {
public:
    int rob(vector<int>& nums) {
        // Create a memoization map to store already computed results
        std::unordered_map<int, int> memo;
        return recur(nums, nums.size()-1, memo);
    }

    int recur(vector<int> &nums, int n, std::unordered_map<int, int>& memo) {
        if (n < 0) return 0;

        // Check if the result for the current index is already computed
        if (memo.find(n) != memo.end()) {
            return memo[n];
        }

        // Compute the result using memoization
        int result = max(recur(nums, n-2, memo) + nums[n], recur(nums, n-1, memo));

        // Store the result in the memoization map
        memo[n] = result;

        return result;
    }
};
