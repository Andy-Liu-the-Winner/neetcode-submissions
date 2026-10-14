class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = 0
        s = set()
        d = {}
        for i in range(len(arr)):
            e = arr[i]
            if e in d:
                if e in s:
                    s.remove(e)
            else:
                d[e] = 1
                s.add(e)
        
        for e in arr:
            if e in s:
                n += 1
                if n == k:
                    return e
        return ""