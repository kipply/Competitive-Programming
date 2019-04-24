import sys
input = sys.stdin.readline

def findNextCellToFill(grid, i, j):
    for x in range(i, 4):
        for y in range(j, 4):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 4):
        for y in range(0, 4):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(4)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(4)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 2 * (i // 2), 2 * (j // 2) # must be integer division
                        for x in range(secTopX, secTopX+2):
                                for y in range(secTopY, secTopY+2):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i, j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1, 5):
                if isValid(grid, i, j, e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False


def preCheck(grid):
    for i in range(4):
        row = list(filter(lambda a: a != 0, grid[i]))
        col = list(filter(lambda a: a != 0, [grid[x][i] for x in range(4)]))
        if list(set(row)) != row:
            return False
        if list(set(col)) != col:
            return False


n = int(input()) 

for _ in range(n): 
    grid = [];
    for i in range(4): 
        row = input().replace("X", "0").rstrip()
        grid.append(list(map(int, list(row))))

    # print grid
    solveSudoku(grid)
    for row in grid: 
        print("".join(map(str, row)))
