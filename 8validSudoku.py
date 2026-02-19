from collections import defaultdict
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows, columns = {}, {}
    for i in range(9):
        for j in range(9):
            rowNum = board[i][j]
            if rowNum == ".":
                continue
            if rowNum in rows:
                print("rows")
                return False
            rows[rowNum] = 1
        rows.clear()

    for i in range(9):
        for j in range(9):
            colNum = board[j][i]
            if colNum == ".":
                continue
            if colNum in columns:
                print("columns")
                return False
            columns[colNum] = 1
        columns.clear()

    boxes = set()
    for square in range(9):
        for i in range(3):
            for j in range(3):
                row = (square // 3) * 3 + i
                column = (square % 3) * 3 + j
                num = board[row][column]
                if num == ".":
                    continue
                if num in boxes:
                    print("boxes")
                    return False
                else:
                    boxes.add(num)
        boxes.clear()
    return True


board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "5", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(board[0][1])
print(isValidSudoku(board))