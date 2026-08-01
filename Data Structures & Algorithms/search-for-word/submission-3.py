class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        if l == 0: return True
        start = []  # stores used (i,j)s for single flight
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: start.append([(i, j)])
        if len(start) == 0:
            return False
        # from start, dfs from there
        def dfs(board, i, j, word, used):
            # end case
            if len(word) == 0:
                return True
            letter = word[0]
            word = word[1: ]
            if i != 0:
                if letter == board[i - 1][j]:
                    if (i - 1, j) not in used:
                        used = used + [(i - 1, j)]
                        if dfs(board, i - 1, j, word, used + [(i - 1, j)]):
                            return True
            if i != len(board) - 1:
                if letter == board[i + 1][j]:
                    if (i + 1, j) not in used:
                        if dfs(board, i + 1, j, word, used + [(i + 1, j)]):
                            return True
            if j != 0:
                if letter == board[i][j - 1]:
                    if (i, j - 1) not in used:
                        if dfs(board, i, j - 1, word, used + [(i, j - 1)]):
                            return True
            if j != len(board[0]) - 1:
                if letter == board[i][j + 1]:
                    if (i, j + 1) not in used:
                        if dfs(board, i, j + 1, word, used + [(i, j + 1)]):
                            return True      
            return False  

        for elem in start:
            for i, j in elem:
                if dfs(board, i, j, word[1: ], elem):
                    return True
        return False
