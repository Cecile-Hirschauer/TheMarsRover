from dataclasses import dataclass, replace
from mars_rover.plateau import Plateau


@dataclass(frozen=True)
class Rover:
    position_x: int
    position_y: int
    orientation: str
    
    def turn(self, instruction):
        if self.orientation == 'N'and instruction == 'R':
            return replace(self, orientation='E')
        if self.orientation == 'E'and instruction == 'R':
            return replace(self, orientation ='S')
        if self.orientation == 'S'and instruction == 'R':
            return replace(self, orientation ='W')
        if self.orientation == 'W'and instruction == 'R':
            return replace(self, orientation ='N')
        if self.orientation == 'N'and instruction == 'L':
            return replace(self, orientation ='W')
        if self.orientation == 'W'and instruction == 'L':
            return replace(self, orientation ='S')
        if self.orientation == 'S'and instruction == 'L':
            return replace(self, orientation ='E')
        if self.orientation == 'E'and instruction == 'L':
            return replace(self, orientation ='N')
   
    def move(self,max_x, max_y, instruction="M"):
        plateau = Plateau(max_x, max_y)
        if self.position_x < 0 or self.position_x > plateau.max_x or self.position_y < 0 or self.position_y > plateau.max_y:
           raise Exception("You are out of the plateau")
        else:
            if self.orientation == 'N':
                return replace(self, position_y = self.position_y + 1)
            elif self.orientation == 'E':
                return replace(self, position_x = self.position_x + 1)
            elif self.orientation == 'S':
                return replace(self, position_y = self.position_y - 1)
            elif self.orientation == 'W':
                return replace(self, position_x = self.position_x - 1)
           