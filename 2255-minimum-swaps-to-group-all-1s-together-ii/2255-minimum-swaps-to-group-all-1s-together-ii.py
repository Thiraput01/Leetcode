class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)
        w_size = sum(nums)

        for i in range(w_size):
            nums.append(nums[i])

        cur_zero = w_size - sum(nums[0:w_size])
        res = cur_zero
        for i in range(1, n):
            if nums[i-1] == 0:
                cur_zero -= 1
            if nums[i+w_size-1] == 0:
                cur_zero += 1

            res = min(res, cur_zero)
        return res




