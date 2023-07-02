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
        print("Fan 1 - Speed:", first_fan.get_speed())
        print("Fan 1 - Radius:", first_fan.get_radius())
        print("Fan 1 - Color:", first_fan.get_color())
        print("Fan 1 - On:", first_fan.is_on())

        # Display the second object's speed, radius, color, and on properties.
        print("\nFan 2 - Speed:", second_fan.get_speed())
        print("Fan 2 - Radius:", second_fan.get_radius())
        print("Fan 2 - Color:", second_fan.get_color())
        print("Fan 2 - On:", second_fan.is_on())

# Create an instance of TestFan to run the program
TestFan()