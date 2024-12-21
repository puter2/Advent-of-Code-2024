class Record:

    def __init__(self, amount, val):
        self.amount = amount
        self.val = val

    def copy(self):
        return Record(self.amount, self.val)