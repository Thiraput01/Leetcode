class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        def dfs(i, total):
            if i == n:
                out.append(total)
                return
            
            dfs(i+1, total[:])
            dfs(i+1, total + [nums[i]])
             

        dfs(0, [])
        return out