class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        words = set(wordList)

        q = deque([(beginWord, 1)])
        import string
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, steps + 1))
        return 0