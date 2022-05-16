class HistoryManager:
    def __init__(self):
        self.history = [[], [], []]

    def update_dinner_history(self, new_dinner_history):
        self.history[0] = new_dinner_history

    def update_lunch_history(self, new_lunch_history):
        self.history[1] = new_lunch_history

    def update_breakfast_history(self, new_breakfast_history):
        self.history[2] = new_breakfast_history

    def get_history(self):
        return self.history
