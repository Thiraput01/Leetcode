class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for mid in range(1, n-1):

            left_lesser = 0
            right_bigger = 0

            left_bigger = 0
            right_lesser = 0

            for l in range(mid):
                if rating[l] < rating[mid]:
                    left_lesser += 1
                else:
                    left_bigger += 1

            for r in range(mid+1, n):
                if rating[r] > rating[mid]:
                    right_bigger += 1
                else:
                    right_lesser += 1

            res += ( left_lesser*right_bigger ) + ( left_bigger*right_lesser )
        return res