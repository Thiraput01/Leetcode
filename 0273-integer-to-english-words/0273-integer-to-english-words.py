class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
        }

        if num == 0:
            return "Zero"


        def helper(n):
            # 123, 120, 012, 102, 100
            res = []
            hundreds = n // 100
            if hundreds > 0:
                res.append(d[hundreds] + " Hundred")
            extra = n % 100
            if extra >= 20:
                tens, ones = extra // 10, extra % 10
                res.append(d[tens*10])
                if ones > 0:
                    res.append(d[ones])

            elif extra > 0:
                res.append(d[extra])

            return " ".join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        res = []
        i = 0  
        while num > 0:
            subnum = num % 1000
            s = helper(subnum)
            if s:
                res = [s + postfix[i]] + res 
            i += 1
            num = num // 1000

        return " ".join(res)