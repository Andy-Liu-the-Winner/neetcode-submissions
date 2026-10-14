class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) 
            b = carry 
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)
            