class Cell:

    def __init__(self, state, neighbour_states = ()):
        self.state = state
        self.neighbour_states = neighbour_states

    def update_state(self):
        alive_neighbour_count = list(self.neighbour_states).count('+')
        if self.state == '+':
            if alive_neighbour_count < 2 or alive_neighbour_count > 3:
                self.state = '-'
            elif alive_neighbour_count in (2, 3):
                return
        elif self.state == '-' and alive_neighbour_count == 3:
            self.state = '+'
