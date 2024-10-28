import pygame
import random

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Window dimensions
ARRAY_SIZE = 5 # Number of bars in the array
BAR_WIDTH = WIDTH // ARRAY_SIZE  # Width of each bar
FPS = 10  # Frames per second

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bogo Sort Visualization with Comparisons')

# Generate a random array
array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]

# Font settings for displaying text
font = pygame.font.SysFont(None, 36)

# Counter for comparisons
comparison_counter = 0
sorting_complete = False  # Flag to indicate when sorting is done

def draw_array(array, sorted=False):
    """ Draw the array as bars on the screen. """
    screen.fill(BLACK)  # Clear the screen
    for i, height in enumerate(array):
        color = GREEN if sorted else RED
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - height, BAR_WIDTH - 2, height))

    # Display the comparison count at the top right corner
    text = font.render(f'Comparisons: {comparison_counter}', True, WHITE)
    screen.blit(text, (WIDTH - 250, 10))

    pygame.display.flip()  # Update the display

def is_sorted(array):
    """ Check if the array is sorted. """
    global comparison_counter
    for i in range(len(array) - 1):
        comparison_counter += 1  # Increment comparison counter for each comparison
        if array[i] > array[i + 1]:
            return False
    return True

def bogo_sort(array):
    """ Perform the bogo sort algorithm. """
    global sorting_complete
    while not sorting_complete:  # Only run if sorting is not yet complete
        random.shuffle(array)
        draw_array(array)

        pygame.time.delay(1000 // FPS)

        if is_sorted(array):
            sorting_complete = True  # Set flag to indicate sorting is done
            draw_array(array, sorted=True)  # Draw the final sorted array

def main():
    """ Main loop for the Bogo Sort visualization. """
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not sorting_complete:
            # Perform Bogo Sort and display comparisons
            bogo_sort(array)

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
