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
    

    def test__solve__x0_y0(self):
        # arrange
        x = 0
        y = 0
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(1, board.result[x][y][0])
        self.assertTrue(board.is_done)
        
        
    def test__solve__x0_y1(self):
        # arrange
        x = 0
        y = 1
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(2, board.result[x][y][0])
        
        
    def test__solve__x0_y7(self):
        # arrange
        x = 0
        y = 7
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(8, board.result[x][y][0])
 

    def test__solve__x1_y0(self):
        # arrange
        x = 1
        y = 0
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(7, board.result[x][y][0])
        self.assertTrue(board.is_done)

        
    def test__solve__x0_y8(self):
        # arrange
        x = 0
        y = 8
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(9, board.result[x][y][0])
        
        
    def test__solve__x8_y0(self):
        # arrange
        x = 8
        y = 0
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(6, board.result[x][y][0])
        self.assertTrue(board.is_done)
        

    def test__solve__x8_y8(self):
        # arrange
        x = 8
        y = 8
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(2, board.result[x][y][0])
        self.assertTrue(board.is_done)
        
        
    def test__solve__x2_y2(self):
        # arrange
        x = 2
        y = 2
        self.grid[x][y] = 0
        # act
        board = Board(self.grid)
        board.solve()
 
        self.assertEqual(6, board.result[x][y][0])
        self.assertTrue(board.is_done)
            
