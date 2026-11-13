class Solution:
    def totalMoney(self, n: int) -> int:
        num_of_28 = n // 7
        res = num_of_28 * 28
        # + 0 * 7 + 1 * 7 + ... (num_of_28 - 1) * 7
        res += (0 + (num_of_28 - 1) * 7) * num_of_28 // 2
        # last row
        remaining = n % 7
        res += (1 + remaining) * remaining // 2 + num_of_28 * remaining
        return res