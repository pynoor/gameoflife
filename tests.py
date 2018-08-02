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
        result = self.TestBoard.cells[0][0].neighbour_states
        expected_result = ('-', '+', '+')
        self.assertEqual(result, expected_result)

class CellTestCase(unittest.TestCase):
    def setUp(self):
        self.cell = Cell('+', ('-', '+', '+'))

    def test_alive_cell_with_two_alive_neighbours_stays_alive(self):
        self.cell.update_state()
        self.assertEqual(self.cell.state, '+')



if __name__ == '__main__':
    unittest.main()