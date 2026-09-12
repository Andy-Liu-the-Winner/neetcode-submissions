class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        is_smaller = {} # a: b, c, d where a < b and a < c and a < d is True
        for word in words:
            for char in word:
                is_smaller.setdefault(char, set())


        # if we have double containment we return ""
        # else build the string
        for i in range(len(words) - 1):
            j = i + 1
            if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                return ""

            ptr = 0
            while ptr < min(len(words[i]), len(words[j])):
                if words[i][ptr] == words[j][ptr]:
                    ptr += 1
                    continue
                else:
                    is_smaller.setdefault(words[i][ptr], set()).add(words[j][ptr])
                    break
                ptr += 1
        
        # build the string
        visited, visiting = set(), set()
        result = []
        def dfs(char):
            if char in visiting: # double containment
                return False 
            if char in visited:
                return True

            visiting.add(char)

            for neighbor in is_smaller[char]:
                if not dfs(neighbor):
                    return False

            visiting.remove(char)
            visited.add(char)
            result.append(char)
            
            return True
        for char in is_smaller:
            if not dfs(char):
                return ""
        
        return "".join(result[::-1])