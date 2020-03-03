# Sudoku-Solver
Python code to solve any Sudoku puzzle.

You will need to initialize the puzzle with 0s as blank squares.
The tricky bit is the recursion. 
The solve() method checks the whole puzzle for blanks. 
For each blank it tries each possible legal number for a possible solution then calls itself with one fewer blank square. 
If the possible solution doesn’t work out, it sets that square back to 0 for blank and continues on. 
When it finds the solution it stops. 
Sudoku puzzles by convention usually have just one solution. 

Enjoy.

