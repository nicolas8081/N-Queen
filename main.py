import random

class Node:
    def __init__(self, board, heuristic):
        self.board = board
        self.heuristic = heuristic

def hillClimbing():
    ...

def heuristic (board: list[int]) -> int:
    heuristicValue = 0
    
    return heuristicValue

def createBoard(n: int) -> list[int]:
    # place queens according to their rows, and treat list index as columns
    board = []
    for i in range(n):
        randomRow = random.randint(0, n - 1)
        board.append(randomRow)
    return board

def solveNQueens(n : int):
    createBoard(n)

def main():
    print("n Queens problem")
    n = int(input("n : "))
    solveNQueens(n)
main()