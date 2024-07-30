class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        for(int i = 0; i < nums.size(); ++i){
            int tmp = target - nums[i];
            if(m.count(tmp)) return {i, m[tmp]};
            m[nums[i]] = i;
        }
        return {};
    }
};