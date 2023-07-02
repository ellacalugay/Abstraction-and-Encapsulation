# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation

# Pseudocode
from Pet import Pet

# Prompts the user to enter the name, type, and age of his or her pet.
name = input("Enter the name of your pet: ")
animal_type = input("Enter the type of your pet: ")
age = input("Enter the age of your pet: ")

# Create an object of the Pet class
pet = Pet(name, animal_type, age)

# Display the entered information using the accessor methods