from unittest import TestCase
from suduko.board import Board as Board

class RemoveFromColTest(TestCase):
    
    def setUp(self):
        self.grid = [
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
    
    
    def tearDown(self):
        pass
    
    
    def test_remove_one(self):
        # arrange
        x = 8
        y = 0
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board._solve_column(x,y,1)
 
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9], board.result[x][y])


    def test_remove_nine(self):
        # arrange
        x = 3
        y = 3
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board._solve_column(x,y,9)
 
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], board.result[x][y])


    def test_remove_five(self):
        # arrange
        x = 2
        y = 1
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board._solve_column(x,y,5)
 
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 9], board.result[x][y])
