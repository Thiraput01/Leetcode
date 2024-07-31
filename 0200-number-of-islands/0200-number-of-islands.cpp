class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        vector<vector<bool>> visited(r, vector<bool>(c, 0));
        int island = 0;
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                if(!visited[i][j] && grid[i][j] == '1'){
                    island++;
                    dfs(i, j, visited, grid);
                }
            }
        }
        return island;
    }
    
    void dfs(int i, int j, vector<vector<bool>> &visited, vector<vector<char>>& grid){
        int r = visited.size();
        int c = visited[0].size();
        visited[i][j] = 1;
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, 1, -1};
        for(int k=0; k<4; ++k){
            int nI = i + dr[k];
            int nJ = j + dc[k];
            if(nI < 0 || nJ < 0 || nI >= r || nJ >= c) continue;
            if(!visited[nI][nJ] && grid[i][j] == '1') dfs(nI, nJ, visited, grid);
        }
    }
};