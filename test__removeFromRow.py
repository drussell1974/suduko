from unittest import TestCase
from suduko.board import Board as Board

class RemoveFromRowTest(TestCase):
    
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
    
    
    def test_removeOne(self):
        # arrange
        self.grid[0][0] = 0
        # act
        board = Board(self.grid)
        board.removeFromRow(0,0,1)
 
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9], board.result[0][0])


    def test_removeNine(self):
        # arrange
        self.grid[0][0] = 0
        # act
        board = Board(self.grid)
        board.removeFromRow(0,0,9)
 
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], board.result[0][0])
