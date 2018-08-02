import unittest
from board import Board
from cell import Cell

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.TestBoard = Board([['+', '-', '-', '+'],
                            ['+', '+', '+', '+'],
                            ['-', '-', '+', '-'],
                            ['+', '-', '-', '-']])

    def test_board_sets_correct_neighbours(self):
        self.TestBoard.set_neighbours()
        result = self.TestBoard.cells[0].neighbours
        expected_result = ('-', '+', '+')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()