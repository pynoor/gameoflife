class Cell:

    def __init__(self, state, neighbours):
        self.state = state
        self.neighbours = []

    def request_new_state(self):
        pass

    def update_state(self):
        self.state = self.request_new_state()