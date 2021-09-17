from mars_rover.plateau import Plateau
from mars_rover.rover import Rover


def read_instruction():
    
    with open('instructions.txt') as f:
        lines = f.read().split('\n')
        print('lines', lines)
        
        
        # Plateau instructions
        upper_right_input = lines[0].split()
        max_x = int(upper_right_input[0])
        max_y = int(upper_right_input[1])
        plateau = Plateau(max_x, max_y)
        
        # Rovers instructions 
        rovers_instructions = []
        for i in range(1, len(lines), 2):
            rovers_instructions.append(tuple(lines[i:i+2]))
        
       
        print(rovers_instructions)
            
            
        
        

read_instruction()
        