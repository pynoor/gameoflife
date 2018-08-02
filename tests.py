import unittest
from board import Board

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.TestBoard = Board([4, 4], ['+', '-', '-', '+',
                            '+', '+', '+', '+',
                            '-', '-', '+', '-',
                            '+', '-', '-', '-'])

    def test_board_sets_correct_neighbours(self):
        result = [set([neighbour.state for neighbour in self.TestBoard.cells[0].neighbours]),
         set([neighbour.state for neighbour in self.TestBoard.cells[3].neighbours])]
        expected_result = [('-', '+', '+'), ('-', '+', '+')]
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()