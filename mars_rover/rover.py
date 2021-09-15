class Rover:
    
    orientations = ('N', 'E', 'S', 'W')
    
    def __init__(self, x, y, orientation):
        self.initial_coordinates = (x, y)
        self.orientation = orientation