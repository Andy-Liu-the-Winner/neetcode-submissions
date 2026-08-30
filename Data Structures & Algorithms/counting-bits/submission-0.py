class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            binary_num = bin(i)
            num = str(binary_num).count("1")
            dp[i] = num
        return dp
