class Solution:
    def rob(self, nums: List[int]) -> int:
        def house(nums):
            rob1, rob2 = 0, 0
            #rob1 = rob house i, rob2 = not rob house i
            for i in nums:
                tmp = max(rob1+i, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
    
        return max(nums[0], house(nums[1:]), house(nums[:-1]))
