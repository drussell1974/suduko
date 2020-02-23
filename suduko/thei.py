from .board import Board

class TheISuduko(Board):
    def __init__(self, board):
        """ set up 9x9 board """
        Board.__init__(self,board)
        
        # add the getI function to the check array
        self._check_func.append(self._solve_theI)
        
        
    def _solve_theI(self, x, y, num):
        """ get the I array and elimiate number from cells
        
        Keyword arguments:
        x -- the row of the current cell
        y -- the column of the current cell
        """
        theI = [(1,4),
                (3,3),(3,4),
                (4,4),
                (5,4),
                (6,4),
                (7,3),(7,4),(7,5)]
        
        if (x, y) in theI:
            for c in theI:
                self._removeNumberFromCell(c[0], c[1], num)
