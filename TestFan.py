# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation

# Pseudocode
from Fan import Fan
# Create a class that creates two Fan Objects.
class TestFan:
    def __init__(self):
        # For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        first_fan = Fan(Fan.FAST, 10, 'yellow', True)
        # For the second object, assign the medium speed, radius 5, color blue, and turn it off.
        second_fan = Fan(Fan.MEDIUM, 5, 'blue', False)
# Display the first object's speed, radius, color, and on properties.
# Display the second object's speed, radius, color, and on properties.
# Create an instance of TestFan to run the program