from cell import Cell

class Board:

    def __init__(self, list_of_cell_state_rows):
        self.list_of_cell_state_rows = list_of_cell_state_rows
        self.cells = []

        for cell_state_row in self.list_of_cell_state_rows:
            new_cell_row = []
            for cell_state in cell_state_row:
                new_cell = Cell(cell_state)
                new_cell_row.append(new_cell)
            self.cells.append(new_cell_row)
        self.set_neighbours()


    def set_neighbours(self):
        for cell_row in self.cells:
            for cell in cell_row:
                cell_index = cell_row.index(cell)
                cell_row_index = self.cells.index(cell_row)
                if cell_index == 0:
                    if cell_row_index == 0:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[0][1],
                            self.list_of_cell_state_rows[1][0],
                            self.list_of_cell_state_rows[1][1],
                            )
                    elif cell_row_index != len(self.list_of_cell_state_rows) - 1:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][0],
                            self.list_of_cell_state_rows[cell_row_index-1][1],
                            self.list_of_cell_state_rows[cell_row_index][1],
                            self.list_of_cell_state_rows[cell_row_index+1][0],
                            self.list_of_cell_state_rows[cell_row_index+1][1]
                        )
                    else:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][0],
                            self.list_of_cell_state_rows[cell_row_index-1][1],
                            self.list_of_cell_state_rows[cell_row_index][1]
                        )
                elif cell_index == len(cell_row) - 1:
                    if cell_row_index == 0:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[0][cell_index-1],
                            self.list_of_cell_state_rows[1][cell_index],
                            self.list_of_cell_state_rows[1][cell_index-1]
                            )
                    elif cell_row_index != len(self.list_of_cell_state_rows) - 1:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index+1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index+1][cell_index-1]
                        )
                    else:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index][cell_index-1]
                        )
                else:
                    if cell_row_index == 0:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[0][cell_index-1],
                            self.list_of_cell_state_rows[0][cell_index+1],
                            self.list_of_cell_state_rows[1][cell_index],
                            self.list_of_cell_state_rows[1][cell_index+1],
                            self.list_of_cell_state_rows[1][cell_index-1],
                            )
                    elif cell_row_index != len(self.list_of_cell_state_rows) - 1:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index+1],
                            self.list_of_cell_state_rows[cell_row_index][cell_index+1],
                            self.list_of_cell_state_rows[cell_row_index][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index+1][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index+1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index+1][cell_index+1]
                        )
                    else:
                        cell.neighbour_states = (
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index-1],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index+1],
                            self.list_of_cell_state_rows[cell_row_index-1][cell_index],
                            self.list_of_cell_state_rows[cell_row_index][cell_index+1],
                            self.list_of_cell_state_rows[cell_row_index][cell_index-1]
                            )

    def set_new_states(self):
        for cell_row in self.cells:
            for cell in cell_row:
                cell.update_state()

    def generate_new_board(self):
        self.set_new_states()
        new_board = []
        for cell_row in self.cells:
            new_cell_state_row = []
            for cell in cell_row:
                new_cell_state_row.append(cell.next_state)
            new_board.append(new_cell_state_row)
        return new_board