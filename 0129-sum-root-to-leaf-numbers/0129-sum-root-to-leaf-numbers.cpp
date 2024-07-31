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
    int sumNumbers(TreeNode* root) {
        if(!root) return 0;
        return dfs(root, "");
    }
    
    int dfs(TreeNode* n, string acc){
        if(!n) return 0;
        acc += to_string(n->val);
        if(n->left==NULL && n->right==NULL) return stoi(acc);
        return dfs(n->left, acc) + dfs(n->right, acc);
    }
};