class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def adj(node):
            res = []
            for i in range(n):
                if isConnected[node][i]==1 and i != node:
                    res.append(i)
            return res

        def dfs(u):
            visited.add(u)
            for v in adj(u):
                if v not in visited:
                    dfs(v)

        visited = set()
        cc = 0
        for i in range(n):
            if(i not in visited):
                dfs(i)
                cc += 1
        return cc
        