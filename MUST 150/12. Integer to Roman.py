class Solution:
    def intToRoman(self, num: int) -> str:
        # The problem is easy if we can handle the exceptional cases
        # With other symbol and value we will add the exceptional cases too

        roman = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],
                ['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        res = []
        for symbol, value in reversed(roman):
            if num//value:
                count = (num//value) * symbol
                res.append(count)
                num = num % value

        return ''.join(res)
