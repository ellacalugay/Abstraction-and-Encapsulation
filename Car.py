# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation - Car Class

# Pseudocode
# Create a class named Car
class Car:
# Create a constructor
    def __init__(self, year_model=2022, make='La Voiture Noire', speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # Create accelerate methd that add 5 to the speed data attribute each time it is called.
    def accelerate(self):
        self.__speed += 5

    # Create brake method that subtract 5 to the speed data attribute each time it is called.
    def brake(self):
        self.__speed -= 5

    # Create get_speed method that should return the current speed.
    def get_speed(self):
        return self.__speed