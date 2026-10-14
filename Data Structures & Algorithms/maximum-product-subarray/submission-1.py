class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(nums) == 1:
                    return 0
                side_winner = max(self.maxProduct(nums[:i]), self.maxProduct(nums[i + 1:]))
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
                print(res)
                res = max(res, nums[j] // nums[i]) 
        return max(res, max(product[1:])) if len(product) > 1 else res