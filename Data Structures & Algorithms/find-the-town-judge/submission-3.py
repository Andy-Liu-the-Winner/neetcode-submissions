class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        for person in range(1, n + 1):
            if person not in {a for a, b in trust} and sum(b == person for a, b in trust) == n - 1:
                return person
        return -1