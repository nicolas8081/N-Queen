import random

class Node:
    def __init__(self, board, heuristic):
        self.board = board
        self.heuristic = heuristic

def hillClimbing(current: Node):
    bestNode = Node(current.board.copy(), current.heuristic)
    while True:
        for i in range(len(current.board)):
                for j in range(len(current.board)):
                    if j != current.board[i]:
                        newBoard = current.board.copy() # fresh list for every neighbor
                        newBoard[i] = j 
                        neighborNode = Node(newBoard, heuristic(newBoard))
                        print(f"{newBoard} h= {neighborNode.heuristic}")
                        if neighborNode.heuristic == 0:
                            return neighborNode
                        if neighborNode.heuristic < bestNode.heuristic:
                            bestNode = neighborNode
        if bestNode.heuristic < current.heuristic:
            current = bestNode
        else:
            return bestNode

def heuristic (board: list[int]) -> int:
    heuristicValue = 0
    for queen in range(len(board)):
        for otherQueen in range(queen + 1,len(board)):
            if queen != otherQueen:
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
    heuristicValue = heuristic(board)
    print(f"This is the heuristic: {heuristicValue}")
    currentNode = Node(board,heuristicValue)
    hillClimbing(currentNode)
    
                


def main():
    print("n Queens problem")
    n = int(input("n : "))
    solveNQueens(n)
main()