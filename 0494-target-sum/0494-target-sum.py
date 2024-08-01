class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        stop = len(nums)
        def cal(idx, total):
            if idx == stop:
                return 1 if total == target else 0
            if (idx, total) in memo:
                return memo[(idx, total)]
            memo[(idx, total)] = cal(idx+1, total+nums[idx]) +                                    cal(idx+1, total-nums[idx])
            return memo[(idx, total)]
        return cal(0, 0)