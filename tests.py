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
        self.cell_1 = Cell('+', ('-', '+', '+'))
        self.cell_2 = Cell('-', ('+', '+', '+', '-', '-'))

    def test_alive_cell_with_two_alive_neighbours_stays_alive(self):
        self.cell_1.update_state()
        self.assertEqual(self.cell_1.state, '+')

    def test_dead_cell_with_three_alive_neighbours_is_revived(self):
        self.cell_2.update_state()
        self.assertEqual(self.cell_2.state, '+')


if __name__ == '__main__':
    unittest.main()