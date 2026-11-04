class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for e in strs:
            s = tuple(sorted(e))
            d[s].append(e)
        return list(d.values())