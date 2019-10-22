
class Playground:
    def __init__(self, width, height):
        self.coordinate_system = [[0]*width]*height
        self.height = height
        self.width = width
        self.current_block = None

    def clear(self):
        self.coordinate_system = [[0]*self.width]*self.height
        self.current_block = None
