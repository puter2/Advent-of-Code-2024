class Key:

    def __init__(self, pins : list):
        self.pins = pins.copy()

    def get_pins(self):
        return self.pins