class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(i):
            s = set()
            for m in range(9):
                if board[i][m] == '.':
                    continue
                if board[i][m] in s:
                    # print("check_row")
                    return False
                s.add(board[i][m])
            return True

        def check_col(i):
            s = set()
            for m in range(9):
                if board[m][i] == '.':
                    continue
                if board[m][i] in s:
                    # print("check_col")
                    return False
                s.add(board[m][i])
            return True
        
        def check_3_times_3(i, j):
            s = set()
            for m in range(3):
                for n in range(3):
                    if board[i + m][j + n] == '.':
                        continue
                    if board[i + m][j + n] in s:
                        # print("check 3 * 3")
                        return False
                    s.add(board[i + m][j + n])
            return True
        
        for i in range(9):
            if not check_row(i) or not check_col(i):
                return False

        for i in range(3):
            for j in range(3):
                if not check_3_times_3(i * 3, j * 3):
                    return False

        return True
