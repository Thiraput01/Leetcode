class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #so hard wtf
        xor = 0
        for i in nums:
            xor ^= i
        
        diff = 1
        while not(xor & diff):
            diff = diff << 1
        a, b = 0, 0
        for i in nums:
            if diff & i:
                a ^= i
            else:
                b ^= i
        return [a, b]