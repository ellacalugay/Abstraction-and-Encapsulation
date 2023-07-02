# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation

# Pseudocode
# Create a class named Fan to represent a fan.
class Fan:
# Create three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
# Create a constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Create a get speed method
    def get_speed(self):
        return self.__speed
    
    # Create a set speed method
    def set_speed(self, speed):
        # A private int data field named speed that specifies the speed of the fan.
        self.__speed = speed

    # Create an is on method
    def is_on(self):
        return self.__on
    
# A private bool data field named on that specifies whether the fan is on (the default is False).
# A private float data field named radius that specifies the radius of the fan.
# A private string data field named color that specifies the color of the fan.
# The accessor(getters) and mutator(setters) methods for all four data fields.