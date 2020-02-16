class Board:
    def __init__(self, board):
        """ set up 9x9 board """
        
        self.board = board
       
    
    def getRow(self, n):
        """ get row array """
    
        return self.board[n-1]
    
        
    def getCol(self, n):
        """ get column array """
       
        col = []
        for row in self.board:
            col.append(row[n-1])
        return col
    
        
    def getSqu(self, x, y):
        """ get the square array """
        x = x % 3 * 3
        y = y % 3 * 3
        
        squ = []
        for p in range(x,x+3):
            for q in range(y,y+3):
                squ.append(self.board[p][q])
        return squ


    def print(self):
        for p in range(0,9):
            print(self.board[p])
        