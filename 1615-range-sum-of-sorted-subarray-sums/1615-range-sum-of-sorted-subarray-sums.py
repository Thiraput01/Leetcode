class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        l = []
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = (cur + nums[j]) % MOD
                l.append(cur)
        l.sort()
        res = 0
        for i in range(left-1, right):
            res = (res + l[i]) % MOD
        return res