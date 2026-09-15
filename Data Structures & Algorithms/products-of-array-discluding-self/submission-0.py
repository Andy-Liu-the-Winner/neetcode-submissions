class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = [i for i, x in enumerate(nums) if x == 0]
        if len(zeros) > 1:
            return [0] * len(nums)
        if len(zeros) == 1:
            product = 1
            for i in range(len(nums)):
                if i != zeros[0]:
                    product *= nums[i]
            return [0] * zeros[0] + [product] + [0] * (len(nums) - 1 - zeros[0])
        else:
            running_product = []
            for i in range(len(nums)):
                if i == 0:
                    running_product.append(nums[i])
                else:
                    running_product.append(nums[i] * running_product[i - 1])
            res = []
            for i in range(len(nums)):
                res.append(running_product[-1] // nums[i])
            return res