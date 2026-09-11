class tree:
    def __init__(self, value):
        self.d = {value: {}}

class WordDictionary:

    def __init__(self):
        self.tree = tree("")

    def addWord(self, word: str) -> None:
        ptr = self.tree.d
        for ch in word:
            if ch not in ptr:
                ptr[ch] = {}
                ptr = ptr[ch]
            elif ch in ptr:
                ptr = ptr[ch] 
        ptr["#"] = {}

    def search(self, word: str) -> bool:
        ptr = self.tree.d
        
        def dfs(ptr, word):
            if len(word) == 0:
                    return "#" in ptr
            index = 0
            for ch in word:
                if ch in ".":
                    for e in ptr:
                        if e != "#" and dfs(ptr[e], word[index + 1:]):
                            return True 
                    return False
                if ch not in ptr:
                    return False
                ptr = ptr[ch]
                index += 1
            return "#" in ptr
        return dfs(ptr, word)

        
