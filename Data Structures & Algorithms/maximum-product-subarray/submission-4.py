class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(nums) == 1:
                    return 0
                if i == 0:
                    return self.maxProduct(nums[i + 1:])
                if i + 1 == len(nums):
                    return self.maxProduct(nums[:i])
                l = self.maxProduct(nums[:i])
                r = self.maxProduct(nums[i + 1:])
                side_winner = max(l, r)
                return max(side_winner, 0)
        product = []
        for i in range(len(nums)):
            if i == 0:
                product.append(nums[0])
                continue
            product.append(product[i - 1] * nums[i])
        
        res = product[-1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                res = max(res, product[j] // product[i]) 
        return max(res, max(product[1:])) if len(product) > 1 else res