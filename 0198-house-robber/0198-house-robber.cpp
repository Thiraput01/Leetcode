class Solution {
public:
    int rob(vector<int>& nums) {
        unordered_map<int, int> memo;
        return recur(nums, nums.size()-1, memo);
    }

    int recur(vector<int> &nums, int n, unordered_map<int, int>& memo) {
        if (n < 0) return 0;

        if (memo.find(n) != memo.end()) return memo[n];
        
        int result = max(recur(nums, n-2, memo) + nums[n], recur(nums, n-1, memo));


        memo[n] = result;

        return result;
    }
};
