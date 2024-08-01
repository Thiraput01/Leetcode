class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) return 0;
        return getSum(root, false);
    }

    int getSum(TreeNode* node, bool isLeft) {
        if (!node) return 0;
        if (!node->left && !node->right && isLeft) return node->val;
        return getSum(node->left, true) + getSum(node->right, false);
    }
};
