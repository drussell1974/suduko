class Board:
    def __init__(self, board):
        """ set up 9x9 board and results """
        # the starting board
        self.board = board
        
        # create results board
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
        self.remove_func = []
        self.remove_func.append(self.removeFromRow)
        self.remove_func.append(self.removeFromCol)
        self.remove_func.append(self.removeFromSqu)
        

    def removeFromRow(self, x, y, num):
        """ get row array """
        for z in range(0, 9):
            if num in self.result[x][z] and len(self.result[x][z]) > 1:
                self.result[x][z].remove(num)
                self.is_done = False


    def removeFromCol(self, x, y, num):
        """ get column array """
        for z in range(0, 9):
            if num in self.result[z][y] and len(self.result[z][y]) > 1:
                self.result[z][y].remove(num)
                self.is_done = False

        
    def removeFromSqu(self, x, y, num):
        """ get the square array """
        x = int(x/3) % 3 * 3
        y = int(y/3) % 3 * 3
        for p in range(x,x+3):
            for q in range(y,y+3):                
                if num in self.result[p][q] and len(self.result[p][q]) > 1:
                    self.result[p][q].remove(num)
                    self.is_done = False

            
    def check(self):
        while(True):
            self.is_done = True
            # iterate all cells
            for x in range(0, 9):
                for y in range(0, 9):
                    # check corresponding cells if cell has one number
                    if len(self.result[x][y]) == 1:
                        number = self.result[x][y][0]
                        # remove number from corressponding cells
                        for f in self.remove_func:
                            # call function
                            f(x, y, number)
            # exit if no changes are made on final pass                            
            if self.is_done == True:
                break
   
   
    def get_result(self, help=False):
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
        return str_result
        
    