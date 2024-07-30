class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        for i in range(len(nums)):
            nums[i] = tmp[i]
        