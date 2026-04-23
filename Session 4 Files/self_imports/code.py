# Just write the name of the file. Notice what hovering does!
import config
from math_functions import add, subtract, multiply, divide
from car import Car

# If it is in a subfolder, write the path with periods
import sub_import.file as sb

if __name__ == '__main__':
    # Variables from direct imports
    if config.GAMEMODE == 'CREATIVE':
        print('Cheats enabled!')
        
    if not config.PVP:
        print('You cannot hurt each other!')

    print(f'Simulation distance: {config.SIMULATION_DISTANCE}')
    print()

    # Methods from direct import
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))
    print()

    # Class from direct import
    honda = Car('Honda', 'Civic', 2022)
    print(honda.goVroom(5))
    print()

    # Variable from sub import
    print(sb.test)