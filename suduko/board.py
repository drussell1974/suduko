class Board:
    def __init__(self, board):
        """ set up 9x9 board
        
        Keyword arguments:
        board -- the starting board.
        
        Use multi-dimensional array - use 0 for empty cell
        e.g. board = [
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
        """
        # variables for statistics
        self.no_of_steps = 0
        self.no_of_comparisons = 0
        
        # create results board. Replace empty cell with 0-9 (these will be eliminated during the solve)
        self.result = []
        for row in board:
            results_row = []
            for c in row:
                if c == 0:
                    results_row.append(([1,2,3,4,5,6,7,8,9]))
                else:
                    results_row.append([c])
            self.result.append(results_row)
            
        # add check functions
        self._solve_func = []
        self._solve_func.append(self._solve_row)
        self._solve_func.append(self._solve_column)
        self._solve_func.append(self._solve_square)
        

    def _solve_row(self, x, y, num):
        """ get row array and elimiate number from cells
        
        Keyword arguments:
        x -- the row of the current cell
        y -- the column of the current cell (VOID)
        """
        for y1 in range(0, 9):
            self._removeNumberFromCell(x, y1, num)


    def _solve_column(self, x, y, num):
        """ get column array and elimiate number from cells
        
        Keyword arguments:
        x -- the row of the current cell (VOID)
        y -- the column of the current cell
        """
        for x1 in range(0, 9):
            self._removeNumberFromCell(x1, y, num)  

        
    def _solve_square(self, x, y, num):
        """ get the square array and elimiate number from cells
        
        Keyword arguments:
        x -- the row of the current cell
        y -- the column of the current cell
        """
        # start at top corner of square
        x = int(x/3) % 3 * 3 # start at x
        y = int(y/3) % 3 * 3 # start at y
        for x1 in range(x,x + 3):
            for y1 in range(y,y + 3):
                self._removeNumberFromCell(x1, y1, num)
                

    def _removeNumberFromCell(self, x, y, num):
        """ remove the number from the cell """
        self.no_of_comparisons = self.no_of_comparisons + 1
        if num in self.result[x][y] and len(self.result[x][y]) > 1:
            self.result[x][y].remove(num)
            self.is_done = False

            
    def solve(self):
        """ solve the board """
        while(True):
            self.is_done = True
            # iterate all cells until done
            # if there are any changes the is_done is set to false
            for x in range(0, 9):
                for y in range(0, 9):
                    self.no_of_steps = self.no_of_steps + 1
                    # check corresponding cells if cell has one number
                    if len(self.result[x][y]) == 1:
                        # get the only number in the array 
                        number = self.result[x][y][0]
                        # call functions to remove number from corressponding cells
                        for f in self._solve_func:
                            f(x, y, number)
            # exit if no changes have been made on final pass                            
            if self.is_done == True:
                break
   
   
    def get_result(self, help=False):
        """
        """
        str_result = ""
        for x in range(0,9):
            if x % 3 == 0:
                str_result = str_result + "\n" 
            for y in range(0,9):
                if y % 3 == 0:
                    str_result = str_result + " "
                number = self.result[x][y]
                if len(self.result[x][y]) > 1 and help == False:
                    number = [0]
                str_result = str_result + str(number) + " "
            str_result = str_result + "\n"
        str_result = str_result + "\nStatisics:\n Solved in {} steps, {} comparisons made".format(self.no_of_steps, self.no_of_comparisons)
        str_result = str_result + "\n Comparisons made per step {}".format(self.no_of_comparisons / self.no_of_steps)
        return str_result
    