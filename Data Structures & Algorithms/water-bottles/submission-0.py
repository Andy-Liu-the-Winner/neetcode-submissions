class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # eff bottle is numExchange - 1
        return numBottles + (numBottles - 1) // (numExchange - 1)