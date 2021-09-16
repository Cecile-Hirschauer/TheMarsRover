import  unittest
from mars_rover.plateau import Plateau


class TestPlateau(unittest.TestCase):
    
    def test_get_grid_dimension(self):
        plateau = Plateau(5, 5)
        
        self.assertEqual(plateau.max_x, 5)
        self.assertEqual(plateau.max_y, 5)
        
if __name__ == '__main__':
    unittest.main()