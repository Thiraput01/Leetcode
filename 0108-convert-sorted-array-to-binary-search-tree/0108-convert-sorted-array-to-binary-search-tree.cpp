/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int mid = nums.size()/2;
        return gen(0, nums.size()-1, nums);
    }
    
    TreeNode* gen(int l, int r, vector<int> &nums){
        if(l>r) return NULL;
        int mid = (l+r)/2;
        auto root = new TreeNode(nums[mid]);
        root->left = gen(l, mid-1, nums);
        root->right = gen(mid+1, r, nums);
        return root;
    }
};