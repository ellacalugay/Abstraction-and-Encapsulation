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

# Define a function to handle form submission
def submit_form():
    # Retrieve the entered information
    name = name_entry.get()
    animal_type = type_entry.get()
    age = age_entry.get()

    # Create an object of the Pet class
    pet = Pet(name, animal_type, age)

    # Display the pet information in a new window
    display_pet_information(pet.get_name(), pet.get_animal_type(), pet.get_age())

# Create the main tkinter window
root = tk.Tk()
root.title("Pet Information Form")

# Create labels and entry fields for the input
name_label = tk.Label(root, text="Name:",  font=('Times', 12, 'bold'), bg='Blue')
name_label.pack()

# Name entry
name_entry = tk.Entry(root)
name_entry.pack()

type_label = tk.Label(root, text="Type:", font=('Times', 12, 'bold'), bg='Red')
type_label.pack()

# Animal type entry
type_entry = tk.Entry(root)
type_entry.pack()

age_label = tk.Label(root, text="Age:", font=('Times', 12, 'bold'), bg='Yellow')
age_label.pack()

# Age entry
age_entry = tk.Entry(root)
age_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form, bg='green', fg='white')
submit_button.pack(side=tk.LEFT, padx=5)

def clear_form():
    # Clear the entry fields
    name_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Create a clear button
clear_button = tk.Button(root, text="Clear", command=clear_form, bg='red', fg='white')
clear_button.pack(side=tk.RIGHT, padx=5)