class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> v(n+1);
        for(auto &i : nums){
            v[i]++;
        }
        vector<int> ans(2);
        for(int i=1; i<n+1; ++i){
            if(v[i]>1) ans[0] = i;
            if(!v[i]) ans[1] = i;
        }
        return ans;
    }
};