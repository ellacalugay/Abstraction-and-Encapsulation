# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #9 | Abstraction and Encapsulation - Fan Class

# Pseudocode
from Fan import Fan
import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Set the window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# Create the Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fan Test")

# Create a class that creates two Fan Objects.
class TestFan:
    def __init__(self):
        # For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        first_fan = Fan(Fan.FAST, 10, 'yellow', True)
        # For the second object, assign the medium speed, radius 5, color blue, and turn it off.
        second_fan = Fan(Fan.MEDIUM, 5, 'blue', False)

        # Create a clock object to control the frame rate
        clock = pygame.time.Clock()

        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the window
            window.fill(LIGHT_BLUE)

            # Render the text
            font = pygame.font.SysFont(None, 30)
        
            # Display the first object's speed, radius, color, and on properties.
            text1 = font.render("Fan 1 - Speed: " + str(first_fan.get_speed()), True, YELLOW)
            text2 = font.render("Fan 1 - Radius: " + str(first_fan.get_radius()), True, YELLOW)
            text3 = font.render("Fan 1 - Color: " + first_fan.get_color(), True, YELLOW)
            text4 = font.render("Fan 1 - On: " + str(first_fan.is_on()), True, YELLOW)

            # Display the second object's speed, radius, color, and on properties.
            text5 = font.render("Fan 2 - Speed: " + str(second_fan.get_speed()), True, BLUE)
            text6 = font.render("Fan 2 - Radius: " + str(second_fan.get_radius()), True, BLUE)
            text7 = font.render("Fan 2 - Color: " + second_fan.get_color(), True, BLUE)
            text8 = font.render("Fan 2 - On: " + str(second_fan.is_on()), True, BLUE)

            # Blit the text onto the window
            window.blit(text1, (10, 10))
            window.blit(text2, (10, 30))
            window.blit(text3, (10, 50))
            window.blit(text4, (10, 70))
            window.blit(text5, (10, 110))
            window.blit(text6, (10, 130))
            window.blit(text7, (10, 150))
            window.blit(text8, (10, 170))

            # Update the display
            pygame.display.flip()

            # Control the frame rate
            clock.tick(60)
        
# Create an instance of TestFan to run the program
TestFan()