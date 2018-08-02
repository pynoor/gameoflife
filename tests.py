import unittest
from board import Board

class TestCase(unittest.TestCase):
    def setUp(self):
        self.TestBoard = Board(['+', '-', '-', '+',
                            '+', '+', '+', '+',
                            '-', '-', '+', '-',
                            '+', '-', '-', '-'])

    def test_board_sets_correct_neighbours(self):
        result = [set([neighbour.state for neighbour in self.TestBoard.cells[0].neighbours]),
         set([neighbour.state for neighbour in self.TestBoard.cells[3].neighbours])]
        expected_result = [('-', '+', '+'), ('-', '+', '+')]
        self.assertEqual(result, expected_result)
