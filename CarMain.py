# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation - Car Class

# Pseudocode
from Car import Car
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 600
window_height = 680
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("All About Car")

# Create a Car object
my_car = Car(2022, "Bugatti")

# Call the accelerate method five times and display the current speed
print("--Accelerate--")
for i in range(1, 6):
    my_car.accelerate()
    print(f"[{i}] Current speed of the car:", my_car.get_speed())

# Call the brake method five times and display the current speed
print("\n\n--Brake--")
for i in range(1, 6):
    my_car.brake()
    print(f"[{i}] Current speed of the car:", my_car.get_speed())
