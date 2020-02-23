from suduko.board import Board as Board
#from thei import TheIBoard as Board

# create the starting grid
grid0 = [
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
]

grid1 = [
    [1,2,3, 4,5,6, 7,8,9],
    [7,8,9, 1,2,3, 4,5,6],
    [4,5,6, 7,8,9, 1,2,3],
    
    [2,3,1, 5,6,4, 8,9,7],
    [8,9,7, 2,3,1, 5,6,4],
    [5,6,4, 8,9,7, 2,3,1],
    
    [3,1,2, 6,4,5, 9,7,8],
    [9,7,8, 3,1,2, 6,4,5],
    [6,4,5, 9,7,8, 3,1,2],
]

# phase 1

easier1 = [
    [6,7,1, 8,0,0, 0,0,3],
    [0,0,0, 0,0,0, 6,0,0],
    [0,4,0, 0,3,6, 0,0,8],
    
    [0,0,6, 0,0,8, 0,1,2],
    [0,0,7, 5,0,4, 8,0,0],
    [8,5,0, 1,0,0, 4,0,0],
    
    [3,0,0, 2,1,0, 0,5,0],
    [0,0,4, 0,0,0, 0,0,0],
    [1,0,0, 0,0,7, 2,8,6],
]

harder1 = [
    [4,1,0, 0,7,0, 0,2,6],
    [7,0,0, 8,0,0, 4,3,0],
    [2,3,0, 0,5,0, 0,0,8],
    
    [0,0,0, 0,0,7, 0,5,4],
    [0,0,0, 5,0,6, 0,0,0],
    [9,4,0, 1,0,0, 0,0,0],
    
    [5,0,0, 0,1,0, 0,4,3],
    [0,9,4, 0,0,5, 0,0,7],
    [8,7,0, 0,3,0, 0,6,5],
]

harder2 = [
    [5,0,2, 0,0,0, 0,7,0],
    [0,0,0, 0,0,9, 5,0,6],
    [0,0,0, 2,5,7, 0,0,1],
    
    [4,5,3, 0,0,0, 0,0,7],
    [0,0,0, 0,9,0, 0,0,0],
    [2,0,0, 0,0,0, 1,6,4],
    
    [8,0,0, 5,2,4, 0,0,0],
    [1,0,5, 3,0,0, 0,0,0],
    [0,2,0, 0,0,0, 4,0,8],
]

easier2 = [
    [6,2,3, 9,0,0, 0,0,0],
    [9,0,0, 8,0,0, 0,0,5],
    [0,0,4, 1,0,0, 6,0,0],
    
    [0,4,8, 0,5,0, 0,0,0],
    [1,3,0, 0,9,0, 0,6,7],
    [0,0,0, 0,1,0, 2,5,0],
    
    [0,0,7, 0,0,1, 8,0,0],
    [5,0,0, 0,0,9, 0,0,6],
    [0,0,0, 0,0,2, 5,9,4],
]

# start the board

board = Board(easier1)
board.solve()

print(board.get_result(help=True))
