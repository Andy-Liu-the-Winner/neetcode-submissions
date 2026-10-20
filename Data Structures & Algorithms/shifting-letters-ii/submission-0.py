class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for i in range(len(s) + 1)]
        for st,e,d in shifts:
            if not d:
                prefix[st] -= 1
                prefix[e + 1] += 1
            else:
                prefix[st] += 1
                prefix[e + 1] -= 1
        print(prefix)
        res = ""
        curr = 0
        for i, c in enumerate(prefix[:-1]):
            curr += c
            res += (chr((ord(s[i])-ord("a") + curr)%26 + ord("a")))
        return res
                
