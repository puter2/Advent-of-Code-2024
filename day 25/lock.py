class Lock:

    def __init__(self, spaces : list):
        self.spaces = spaces.copy()
    
    def get_spaces(self):
        return self.spaces