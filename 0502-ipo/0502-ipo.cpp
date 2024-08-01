class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        ios_base::sync_with_stdio(false);
        priority_queue<int> maxHeap;
        multiset<pair<int, int>> minHeap;
        int n = profits.size();
        
        for(int i = 0; i < n; ++i) minHeap.insert({capital[i], profits[i]});
        
        for(int i = 0; i < k; ++i) {
            while(!minHeap.empty() && minHeap.begin()->first <= w) {
                maxHeap.push(minHeap.begin()->second);
                minHeap.erase(minHeap.begin());
            }
            if(maxHeap.empty()) break;
            
            w += maxHeap.top();
            maxHeap.pop();
        }

        return w;
    }
};
