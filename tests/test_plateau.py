import  unittest
from mars_rover.plateau import Plateau


class TestPlateau(unittest.TestCase):
    
    def test_get_grid_dimension(self):
        plateau = Plateau(5, 5)
        plateau.get_grid_dimension()
        
        self.assertEqual(plateau.grid_dimension, (5, 5))
        self.assertEqual(plateau.grid_dimension[0], 5)
        self.assertEqual(plateau.grid_dimension[1], 5)

if __name__ == '__main__':
    unittest.main()