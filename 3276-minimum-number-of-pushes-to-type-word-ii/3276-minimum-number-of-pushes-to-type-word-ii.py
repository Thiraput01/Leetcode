class Solution:
    def minimumPushes(self, word: str) -> int:
        m = Counter(word)
        freq = sorted(m, key=lambda x: m[x], reverse=True)
        c = 0
        mul = 1
        res = 0
        for i in freq:
            c += 1
            if c > 8:
                mul += 1
                c = 1

            print('Cur:', i, 'mul:', mul)
            res += m[i] * mul

        return res