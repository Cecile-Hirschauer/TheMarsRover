import unittest
from mars_rover.rover import Rover
from mars_rover.plateau import Plateau


class TestRover(unittest.TestCase):
      
    def test_rover_initial_position(self):
        rover = Rover(1, 2, 'N')
        self.assertEqual(rover.position_x, 1)
        self.assertEqual(rover.position_y, 2)
        self.assertEqual(rover.orientation, 'N')
        
    def test_turn_right_N_to_E(self):
        rover = Rover(1, 2, 'N')
        rover = rover.turn('R')
        self.assertEqual('E', rover.orientation)
        
    def test_turn_right_E_to_S(self):
        rover = Rover(1, 2, 'E')
        rover = rover.turn('R')
        self.assertEqual('S', rover.orientation)
        
    def test_turn_right_S_to_W(self):
        rover = Rover(1, 2, 'S')
        rover = rover.turn('R')
        self.assertEqual('W', rover.orientation)
        
    def test_turn_right_W_to_N(self):
        rover = Rover(1, 2, 'W')
        rover = rover.turn('R')
        self.assertEqual('N', rover.orientation)
    
    def test_turn_left_N_to_W(self):
        rover = Rover(1, 2, 'N')
        rover = rover.turn('L')
        self.assertEqual('W', rover.orientation)
        
    def test_turn_left_W_to_S(self):
        rover = Rover(1, 2, 'W')
        rover = rover.turn('L')
        self.assertEqual('S', rover.orientation)
        
    def test_turn_left_S_to_E(self):
        rover = Rover(1, 2, 'S')
        rover = rover.turn('L')
        self.assertEqual('E', rover.orientation)
        
    def test_turn_left_E_to_N(self):
        rover = Rover(1, 2, 'E')
        rover = rover.turn('L')
        self.assertEqual('N', rover.orientation)
        
    def test_move_orintation_N(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, 'N')
        rover = rover.move(plateau.max_x, plateau.max_y,'M')
        # self.assertRaises(Exception)
        self.assertEqual(rover.position_y, 3)
        
    def test_move_orintation_E(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, 'E')
        rover = rover.move(plateau.max_x, plateau.max_y,'M')
        # self.assertRaises(Exception)
        self.assertEqual(rover.position_x, 2)
    
    def test_move_orintation_S(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, 'S')
        rover = rover.move(plateau.max_x, plateau.max_y,'M')
        # self.assertRaises(Exception)
        self.assertEqual(rover.position_y, 1)
        
    def test_move_orintation_W(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, 'W')
        rover = rover.move(plateau.max_x, plateau.max_y,'M')
        # self.assertRaises(Exception)
        self.assertEqual(rover.position_x, 0)


if __name__ == '__main__':
    unittest.main()