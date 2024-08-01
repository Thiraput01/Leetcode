class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        priority_queue<int> pq;
        unordered_map<int, int> um;
        for(auto &i : score) pq.push(i);
        int c = 0;
        while(!pq.empty()){
            int u = pq.top(); pq.pop();
            c++;
            um[u] = c;
        }
        vector<string> ans(score.size());
        for(int i=0; i<score.size(); ++i){
            int rank = um[score[i]];
            string ranks = std::to_string(rank);
            if(rank == 1) ans[i] = "Gold Medal";
            else if(rank == 2) ans[i] = "Silver Medal";
            else if(rank == 3) ans[i] = "Bronze Medal";
            else ans[i] = ranks;
        }
        return ans;
    }
};