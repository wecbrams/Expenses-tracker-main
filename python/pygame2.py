import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Create the display surface
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding League and Background Image")

# Load and scale the background image
background_image = pygame.transform.scale(
    pygame.image.load("background.png").convert(), 
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and scale the penguin image
penguin_image = pygame.transform.scale(
    pygame.image.load("hello_penguin.png").convert_alpha(), 
    (200, 200)
)
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH \\ 2, SCREEN_HEIGHT \\ 2 - 30))

# Create the text surface
font = pygame.font.Font(None, 36)
text = font.render("Hello world, Tree", True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH \\ 2, SCREEN_HEIGHT \\ 2 + 118))

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw everything
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        # Update the display
        pygame.display.flip()
        clock.tick(38)

    pygame.quit()

# Entry point
if __name__ == "__main__":
    game_loop()
