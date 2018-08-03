import unittest
from board import Board
from cell import Cell

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.first_board = Board([['+', '-', '-', '+'],
                            ['+', '+', '+', '+'],
                            ['-', '-', '+', '-'],
                            ['+', '-', '-', '-']])
        self.second_board = Board([['-', '-', '+', '-'],
                            ['-','+', '+', '+'],
                            ['+', '-', '+', '-']
                            ])


    def test_board_sets_neighbours(self):
        # Exercise
        '''
        Essentially, what we're testing here is wether or not the command 'self.first_board.set_neighbours()'
        works. We will not explicitly call it here, because it is automatically ran, when the board is created.
        '''

        # Verify
        random_cell = self.first_board.cells[1][2]
        result = random_cell.neighbour_states
        expected_result = ('+', '+', '-', '+', '-', '-', '-', '+')
        self.assertCountEqual(result, expected_result)

    def test_board_generates_new_board(self):
        result = self.second_board.generate_new_board()

        expected_result = [['-', '+', '+', '+'],
                            ['-', '-', '-', '+'],
                            ['-', '-', '+', '+'],
        ]
        self.assertEqual(result, expected_result)


class CellTestCase(unittest.TestCase):
    def setUp(self):
        self.alive_cell = Cell('+', ('-', '+', '+'))
        self.dead_cell = Cell('-', ('+', '+', '+', '-', '-'))

    def test_alive_cell_with_two_alive_neighbours_stays_alive(self):
        self.alive_cell.update_state()
        self.assertEqual(self.alive_cell.next_state, '+')

    def test_dead_cell_with_three_alive_neighbours_is_revived(self):
        self.dead_cell.update_state()
        self.assertEqual(self.dead_cell.next_state, '+')

if __name__ == '__main__':
    unittest.main()
