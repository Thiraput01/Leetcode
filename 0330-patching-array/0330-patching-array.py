class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        mx = 0
        i = 0
        res = 0
        while mx < n:
            if i < len(nums) and nums[i] <= mx+1 :
                mx += nums[i]
                i += 1
            else:
                res += 1
                mx += (mx+1)
        return res