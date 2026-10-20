class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()

        # l1 is smaller
        if len(l2) < len(l1):
            l1, l2 = l2, l1 
        
        left, right = 0, 0
        n1 = len(l1)
        n2 = len(l2)

        while left < n1 and l1[left] == l2[left]:
            left += 1
        
        while right + left < n1 and l1[n1 - 1 - right] == l2[n2 - 1 - right]:
            right += 1
        return left + right == n1