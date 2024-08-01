class Solution:
    def checkSubarraySum(self, nums, k):
        # Initialize the hashmap with the base case
        mod_map = {0: -1}
        current_sum = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if k != 0:
                current_sum %= k
            
            if current_sum in mod_map:
                if i - mod_map[current_sum] > 1:
                    return True
            else:
                mod_map[current_sum] = i
                
        return False