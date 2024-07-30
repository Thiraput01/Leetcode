class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> tmp;
        for(int i=0; i<nums.size()-1; ++i){
          if(nums[i+1] != nums[i]){
            tmp.push_back(nums[i]);
          }
        }
        if(nums.size()>1 && nums[nums.size()-1] != nums[nums.size()-2]){
          tmp.push_back(nums[nums.size()-1]);
        }else{
          tmp.push_back(nums[nums.size()-1]);
        }
        nums = tmp;
        return nums.size();
    }
};