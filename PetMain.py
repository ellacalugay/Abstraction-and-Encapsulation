# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation - Pet Class

# Pseudocode
from Pet import Pet
import tkinter as tk
from tkinter import ttk

# Define a function to display the pet information
def display_pet_information(name, animal_type, age):

    # Initialize tkinter app
    info_window = tk.Tk()
    info_window.title("Pet Information")
    info_window.configure(background='pink')

    # Set style
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))

    # Create an info label to display the pet information
    info_label = tk.Label(info_window, text="Pet Information", font=('Helvetica', 16, 'bold'), bg='light blue')
    info_label.pack(pady=20)

    # Create a name label to display the pet name
    name_label = tk.Label(info_window, text="Your pet name is " + name, font=('Times', 12, 'bold'), bg='yellow')
    name_label.pack()

    # Create a name label to display the pet type
    type_label = tk.Label(info_window, text="Your pet type is " + animal_type, font=('Times', 12, 'bold'), bg='yellow')
    type_label.pack()

    # Create a name label to display the pet age
    age_label = tk.Label(info_window, text="Your pet age is " + age, font=('Times', 12, 'bold'), bg='yellow')
    age_label.pack()

# Prompts the user to enter the name, type, and age of his or her pet.
name = input("Enter the name of your pet: ")
animal_type = input("Enter the type of your pet: ")
age = input("Enter the age of your pet: ")

# Create an object of the Pet class
pet = Pet(name, animal_type, age)

# Display the entered information using the accessor methods
print("Your pet's name is", pet.get_name())
print("Your pet's type is", pet.get_animal_type())
print("Your pet's age is", pet.get_age())

# Create the main tkinter window
root = tk.Tk()
root.title("Pet Information Form")