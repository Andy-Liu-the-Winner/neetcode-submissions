class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            n = nums[i]
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)
        
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in d:
                index = d[diff]
                if diff == n:
                    if len(index) > 1:
                        return [i, index[-1]]
                    else: 
                        continue
                return [i, index[0]]
            

