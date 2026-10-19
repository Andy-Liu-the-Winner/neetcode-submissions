class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        code_prime = code + code
        s = 0
        prefix = []
        for i in range(len(code_prime)):
            s += code_prime[i]
            prefix.append(s)
        res = []
        if k > 0:
            # futuer k sum
            for i in range(len(code)):
                res.append(prefix[k + i] - prefix[i])
        else:
            for i in range(len(code)):
                res.append(prefix[len(code) + i - 1] - prefix[len(code) + i + k - 1])
        return res
            
