from unittest import TestCase
from suduko.board import Board as Board

class CompleteFinalSquareTest(TestCase):
    
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
    

    def test_fill__x0_y0(self):
        # arrange
        self.grid[0][0] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(1, board.result[0][0][0])
        self.assertTrue(board.is_done)
        
        
    def test_fill__x0_y1(self):
        # arrange
        self.grid[0][1] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(2, board.result[0][1][0])
        
        
    def test_fill__x0_y7(self):
        # arrange
        self.grid[0][7] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(8, board.result[0][7][0])
 

    def test_fill__x1_y0(self):
        # arrange
        self.grid[1][0] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(7, board.result[1][0][0])
        self.assertTrue(board.is_done)

        
    def test_fill__x0_y8(self):
        # arrange
        self.grid[0][8] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(9, board.result[0][8][0])
        
        
    def test_fill__x8_y0(self):
        # arrange
        self.grid[8][0] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(6, board.result[8][0][0])
        self.assertTrue(board.is_done)
        

    def test_fill__x8_y8(self):
        # arrange
        self.grid[8][8] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(2, board.result[8][8][0])
        self.assertTrue(board.is_done)
        
        
    def test_fill__x2_y2(self):
        # arrange
        self.grid[2][2] = 0
        # act
        board = Board(self.grid)
        board.check()
 
        self.assertEqual(6, board.result[2][2][0])
        self.assertTrue(board.is_done)
            
