import random
import time

class Node:
    def __init__(self, board, heuristic):
        self.board = board
        self.heuristic = heuristic

# takes a Node, runs the hillclimbing algorithm generating the heuristic of moving every queen and returns the chess board and the steps
def hillClimbing(current: Node):
    bestNode = Node(current.board.copy(), current.heuristic)
    steps = 0
    while True:
        for i in range(len(current.board)):
                for j in range(len(current.board)):
                    if j != current.board[i]:
                        newBoard = current.board.copy()
                        newBoard[i] = j 
                        neighborNode = Node(newBoard, heuristic(newBoard))
                        #print(f"{newBoard} h= {neighborNode.heuristic}")
                        if neighborNode.heuristic == 0:
                            steps += 1
                            return neighborNode.board, steps
                        if neighborNode.heuristic < bestNode.heuristic:
                            bestNode = neighborNode
        if bestNode.heuristic < current.heuristic:
            steps += 1
            current = bestNode
        else:
            return bestNode.board, steps
# helper function that takes a puzzle board and generates an overall heuristic of the board, it returns an integer heuristic 
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

def printBoard(board: list[int]):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[column] == row:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
    print()
    
# takes n as to generate an nxn board
def createBoard(n: int) -> list[int]:
    board = []
    for i in range(n):
        randomRow = random.randint(0, n - 1)
        board.append(randomRow)
    return board

# counts how many other queens would attack a queen at the given column and row
def countConflicts(board: list[int], columnIndex: int, row: int) -> int:
    # how many queens are attacking at the column and rwo
    heuristicValue = 0
    for otherQueen in range(len(board)):
        if otherQueen != columnIndex:
            if row == board[otherQueen]:
                heuristicValue += 1
            else:
                column = abs(columnIndex - otherQueen)
                rowDistance = abs(row - board[otherQueen])
                if rowDistance == column:
                    heuristicValue += 1
    return heuristicValue

# takes a conflicted queens column index and the board, it counts how many queens would attack it on each row of its column
# it returns the row with the fewest conflicts from a list randomly if there are ties
def chooseLowest(columnIndex: int, board: list[int]) -> int:
    lowestHeuristic = float("inf")#infinity as lowest so the first row will be less automatically
    bestRows = []

    for row in range(len(board)):
        heuristicValue = countConflicts(board, columnIndex, row)
        if heuristicValue < lowestHeuristic:
            lowestHeuristic = heuristicValue
            bestRows.clear()
            bestRows.append(row)
        elif heuristicValue == lowestHeuristic:
            bestRows.append(row)

    randomIndex = random.randint(0, len(bestRows) - 1)
    return bestRows[randomIndex]

# takes a board configuration and returns a list of queens that are conflicted within that board. 
def conflictedQueen(board: list[int]) -> list[int]:
    listOfConflictedQueens = []
    for column in range(len(board)):
        value = countConflicts(board, column, board[column])
        if value > 0:
            listOfConflictedQueens.append(column)
    return listOfConflictedQueens

# takes a chess board, and defaults automatically to 1000 steps, it will call helper functions and it will return either completed run or None to show failure
def minConflicts(board: list[int], max_steps: int = 1000):
    current = board.copy()

    for step in range(max_steps):
        conflicted = conflictedQueen(current)
        # if there are no conflicts, its solved so we stop 
        if len(conflicted) == 0:
            return current, step

        randomIndex = random.randint(0, len(conflicted) - 1)
        var = conflicted[randomIndex]
        value = chooseLowest(var, current)
        current[var] = value

    if len(conflictedQueen(current)) == 0:
        return current, max_steps

    return None, max_steps
# calls both algorithms after recieving n from the user, it will not return anything. it will print the results of both. 
def solveNQueens(n: int):
    board = createBoard(n)
    heuristicValue = heuristic(board)
    print("Starting board")
    printBoard(board)
    print(f"it's heuristic value = {heuristicValue}")
    currentNode = Node(board,heuristicValue)
    hillClimbBoard, hillClimbSteps = hillClimbing(currentNode)
    hillClimbHeuristic = heuristic(hillClimbBoard)
    print("Hill Climbing")

    if hillClimbHeuristic == 0:
        print(f"Solved in {hillClimbSteps} steps and this is the final board {hillClimbBoard}")
        printBoard(hillClimbBoard)
    else:
        print(f"The problem got stuck after {hillClimbSteps} steps with heuristic value = {hillClimbHeuristic} and this is the final board {hillClimbBoard}")
        printBoard(hillClimbBoard)

    minConflictsBoard, minConflictsSteps = minConflicts(board)
    print("Min Conflicts")
    if minConflictsBoard is None:
        print(f"The problem failed after {minConflictsSteps} steps")
        printBoard(minConflictsBoard)
    else:
        print(f"Solved in {minConflictsSteps} steps and this is the final board {minConflictsBoard}")
        printBoard(minConflictsBoard)

def solveNQueensForTest(n : int):
    board = createBoard(n)
    heuristicValue = heuristic(board)
    currentNode = Node(board,heuristicValue)

    # hill climbing
    hillClimbSolved = 0
    startTime = time.perf_counter()
    hillClimbBoard, hillClimbSteps = hillClimbing(currentNode)
    finalTime = time.perf_counter() - startTime
    if heuristic(hillClimbBoard) == 0:
        hillClimbSolved +=1 

    # min conflicts
    startTimeMinConflicts = time.perf_counter()
    minConflictsBoard, minConflictsSteps = minConflicts(board)
    finalTimeMinConflicts = time.perf_counter() - startTimeMinConflicts
    if minConflictsBoard == None:
        minConflictsSolved = False
    else:
        minConflictsSolved = True

    return (hillClimbSolved, hillClimbSteps, finalTime, minConflictsSolved, minConflictsSteps, finalTimeMinConflicts)

def runTests(n: int, total: int = 200):
    hillClimbSuccess = 0
    hillClimbTotalSteps = 0
    hillClimbTotalTime = 0

    minConflictsSuccess = 0
    minConflictsTotalSteps = 0
    minConflictsTotalTime = 0

    for i in range(total):
        (hillClimbSolved, hillClimbSteps, hillClimbTime, minConflictsSolved, minConflictsSteps, minConflictsTime) = solveNQueensForTest(n)

        if hillClimbSolved:
            hillClimbSuccess += 1
        hillClimbTotalSteps += hillClimbSteps
        hillClimbTotalTime += hillClimbTime

        if minConflictsSolved:
            minConflictsSuccess += 1
        minConflictsTotalSteps += minConflictsSteps
        minConflictsTotalTime += minConflictsTime

    print(f"n = {n} for {total} boards")

    print("Hill Climbing")
    print(f"Solved: {hillClimbSuccess/total * 100:.1f}%")
    print(f"Average steps: {hillClimbTotalSteps/total:.2f}")
    print(f"Average time: {hillClimbTotalTime/total * 1000:.3f} ms")

    print("Min Conflicts")
    print(f"Solved: {minConflictsSuccess/total * 100:.1f}%")
    print(f"Average steps: {minConflictsTotalSteps/total:.2f}")
    print(f"Average time: {minConflictsTotalTime/total * 1000:.3f} ms")

def main():
    print("n Queens problem")
    n = int(input("n : "))
    solveNQueens(n)
    #runTests(8)
    #runTests(12)
    #runTests(16)
main()