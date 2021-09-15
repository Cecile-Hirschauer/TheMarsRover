import unittest
from mars_rover.rover import Rover

class TestRover(unittest.TestCase):
    
    def test_initialize_rover(self):
        rover = Rover(1, 2, 'N')
        



if __name__ == '__main__':
    unittest.main()