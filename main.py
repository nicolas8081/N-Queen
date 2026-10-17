import random

class Node:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic

def hillClimbing():
    ...

def heuristic ():
    ...

def createBoard(n : int) -> list[int]: 
    # initalize board with 0's 
    board = [0] * n**2
    for column in range(n):
        row = random.randint(0, n-1)
        index = (row * n) + column
        board[index] = 1
    for i in range(len(board)):
        print(board[i], end=" ")
        if (i + 1) % n == 0:
            print()
    return board

def solveNQueens(n : int):
    createBoard(n)

def main():
    print("n Queens problem")
    n = int(input("n : "))
    solveNQueens(n)
main()