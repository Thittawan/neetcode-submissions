class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mapping = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                value = mapping.get(board[i][j], 0) + 1
                mapping[board[i][j]] = value
                if value != 1:
                    return False
            mapping = {}
        for j in range(len(board)):
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                value = mapping.get(board[i][j], 0) + 1
                mapping[board[i][j]] = value
                if value != 1:
                    return False
            mapping = {}
            
        for k in range(9):
            setting = set()
            for i in range(3):
                for j in range(3):
                    row = (k // 3) * 3 + i
                    col = (k % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in setting:
                        return False
                    setting.add(board[row][col])
        return True