import random

class Node:
    def __init__(self, board, heuristic):
        self.board = board
        self.heuristic = heuristic

def hillClimbing():
    ...

def heuristic (board: list[int]) -> int:
    heuristicValue = 0
    for queen in range(len(board)):
        for otherQueen in range(queen + 1,len(board)):
            # checks if queens are on the same row
            if board[queen] == board[otherQueen]:
                heuristicValue += 1
            # check if they are on the same diagonal 
            else:
                column = abs(queen - otherQueen)
                row = abs(board[queen] - board[otherQueen])
                if row == column:
                    heuristicValue += 1
    return heuristicValue

def createBoard(n: int) -> list[int]:
    # place queens according to their rows, and treat list index as columns
    board = []
    for i in range(n):
        randomRow = random.randint(0, n - 1)
        board.append(randomRow)
    for i in range(len(board)):
        print(board[i], end=" ")
        if (i + 1) % n == 0:
            print()
    return board

def solveNQueens(n : int):
    board = createBoard(n)
    print(f"This is the heuristic: {heuristic(board)}")

def main():
    print("n Queens problem")
    n = int(input("n : "))
    solveNQueens(n)
main()