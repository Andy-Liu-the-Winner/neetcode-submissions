class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 :
            return 1.0
        dp = [0.0] * (k + maxPts)
        dp[0] = 1.0
        window_sum = 1.0
        ans = 0.0
        for i in range(1, k + maxPts):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            elif i <= n:
                ans += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                window_sum -= dp[i - maxPts]
        return ans

