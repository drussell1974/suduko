from board import Board

class TheIBoard(Board):
    def __init__(self, board):
        """ set up 9x9 board """
        Board.__init__(self,board)
        
        # add the getI function to the check array
        self.remove_func.append(self.getI)
        
        
    def getI(self, x, y, num):
        """ get the 'i' """
        # TODO: remove num from cell
        cells = [board[1,4],
                board[3,3],board[3,4],
                board[4,4],
                board[5,4],
                board[6,4],
                board[7,3],board[7,4],board[7,5]]