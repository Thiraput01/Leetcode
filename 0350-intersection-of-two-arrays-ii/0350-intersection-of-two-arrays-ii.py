class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(int)
        for i in nums1:
            m[i] += 1
        res = []
        for i in nums2:
            if m[i] > 0:
                res.append(i)
                m[i] -= 1
                    
        return res