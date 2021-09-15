class Plateau:
    
    def __init__(self, x=0, y=0):
        self.grid_dimension = (x, y)
        
    def get_grid_dimension(self):
        return (self.grid_dimension[0], self.grid_dimension[1])