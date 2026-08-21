class PrefixTree:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        v = self.d
        for s in word:
            if s not in v:
                v[s] = {}
            v = v[s]
        v['#'] = True
            
    def search(self, word: str) -> bool:
        if not word: return True
        v = self.d 
        for s in word:
            if s not in v:
                return False
            else:
                v = v[s]
        return '#' in v


    def startsWith(self, prefix: str) -> bool:
        v = self.d 
        for s in prefix:
            if s not in v:
                return False
            else:
                v = v[s]
        return True
