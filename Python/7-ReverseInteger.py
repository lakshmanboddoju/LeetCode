class Solution:
    def reverse(self, x: int) -> int:
        
        isNegative = x < 0
        x = abs(x)
        rev = 0
        
        while (x != 0):
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop
        
        if rev < -2147483648 or rev > 2147483647:
            return 0
        if isNegative :
            return -rev
        return rev
    
