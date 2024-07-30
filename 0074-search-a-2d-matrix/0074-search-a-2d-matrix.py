import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(log(nm))
        n = len(matrix)
        m = len(matrix[0])
        def findrow():
            l = []
            for i in matrix:
                l.append(i[0])
            pos = max(0, bisect.bisect_right(l, target) - 1)
            return pos
        tmp = matrix[findrow()]
        idx = bisect.bisect_left(tmp, target)
        if idx != len(tmp) and tmp[idx] == target:
            return True
        return False