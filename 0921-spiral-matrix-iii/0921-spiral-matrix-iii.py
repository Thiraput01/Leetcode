class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ways = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        #         r        d       l        u
        res = []
        r = rStart
        c = cStart
        step = 1
        i = 0

        res.append([r, c])
        while len(res) < rows * cols:

            for j in range(2):
                for e in range(step):
                    r += ways[i][0]
                    c += ways[i][1]
                    if (0 <= r < rows) and (0 <= c < cols):
                        res.append([r, c])
                i = (i+1) % 4 # 0 1 2 3 0 1 2 3 0 . . .
                
            step += 1

        return res