class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(i, target):
            if i >= n:
                return 0
            if target == 0:
                return 1
            if target < 0:
                return 0
        
            if (i, target) in memo:
                return memo[(i, target)]
        
            memo[(i, target)] = dfs(i, target-coins[i]) + dfs(i+1, target)
            return memo[(i, target)]
    
        return dfs(0, amount)