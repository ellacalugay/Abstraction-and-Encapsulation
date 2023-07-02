# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation

# Pseudocode
from Car import Car

# Create a Car object
my_car = Car(2022, "Bugatti")

# Call the accelerate method five times and display the current speed
print("--Accelerate--")
for i in range(1, 6):
    my_car.accelerate()
    print(f"[{i}] Current speed of the car:", my_car.get_speed())

# Call the brake method five times and display the current speed
