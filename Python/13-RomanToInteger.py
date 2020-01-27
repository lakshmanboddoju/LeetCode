class Solution:
    def romanToInt(self, s: str) -> int:
        doubles = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        singles = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        outputSum = 0
        i = 0
        while i < len(s):
            if temp in doubles:
                outputSum = outputSum + doubles[s[i:i+2]]
                i += 2
            else:
                outputSum = outputSum + singles[s[i]]
                i += 1
        return outputSum
