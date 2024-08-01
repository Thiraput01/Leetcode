class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq;
        for(auto &i: nums){
            pq.push(i);
        }
        int out;
        for(int i=0; i<k; i++){
            out = pq.top();
            pq.pop();
        }
        return out;
    }
};