class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        ios_base::sync_with_stdio(false); cin.tie(0);
        vector<vector<int>> graph(n+1);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<vector<int>> times(n+1, vector<int>(2, INT_MAX));
        queue<pair<int, int>> q; //{node, curtime}
        q.push({1, 0});
        times[1][0] = 0;
        
        while (!q.empty()) {
            auto [curNode, curTime] = q.front(); q.pop();
            
            int newTime = curTime + time;
            if ((curTime / change) % 2) newTime += change - (curTime % change);
            
            
            for (auto &neighbor : graph[curNode]) {
                if (newTime < times[neighbor][0]) {
                    times[neighbor][1] = times[neighbor][0];
                    times[neighbor][0] = newTime;
                    q.push({neighbor, newTime});
                } else if (newTime > times[neighbor][0] && newTime < times[neighbor][1]) {
                    times[neighbor][1] = newTime;
                    q.push({neighbor, newTime});
                }
            }
            
            if (times[n][1] != INT_MAX) return times[n][1];
            
        }
        
        return -1;  // Should never reach here given the problem constraints
    }
};