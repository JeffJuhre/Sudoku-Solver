import numpy as np
   
puzzle =  [[0,0,0,0,0,8,0,0,7],
            [0,7,5,0,6,0,0,0,0],
            [0,3,0,0,0,4,0,0,9],
            [0,0,0,0,5,0,2,0,0],
            [2,0,6,0,0,0,1,0,4],
            [0,0,1,0,9,0,0,0,0],
            [6,0,0,8,0,0,0,1,0],
            [0,0,0,0,7,0,9,8,0],
            [7,0,0,6,0,0,0,0,0]]   
solved = False

def IsPossible(y,x,n):
    global puzzle
    # check row for number already in row
    for i in range(9):
        if puzzle[y][i] == n:
            return False
    # check for number already in column
    for i in range(9):
        if puzzle[i][x] == n:
            return False
    # there are 3x3 local groups, figure local group coordinates for x,y
    localGroupXOffset = (x//3)*3
    localGroupYOffset = (y//3)*3
    # check the 9 squares in the local grid for number already there
    for i in range(3):
        for j in range(3):
            if puzzle[localGroupYOffset + i][localGroupXOffset + j] == n:
                return False
    # number is possible
    return True

def solve():
    global puzzle, solved
    for y in range(9):
       for x in range(9):
            # find next empty square
            if puzzle[y][x] == 0:
                # try each number 1 to 9
                for n in range(1,10):
                    if IsPossible(y,x,n):
                        # try that number and see how it goes
                        puzzle[y][x] = n
                        solve()
                        if solved:
                            return
                        else:
                            # possible solution didn't work out, backtrack
                            puzzle[y][x] = 0
                return
    # all done  
    solved = True
    print('The solution is:')
    print(np.matrix(puzzle)) 

def main():
    solve()

