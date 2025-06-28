import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

# Load font
font = pygame.font.SysFont("Arial", FONT_SIZE)

# Sprite class
class Box(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.rect.x = max(0, min(self.rect.x + dx, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + dy, SCREEN_HEIGHT - self.rect.height))

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Object Collision = You Win")

# Create player and target
player = Box(pygame.Color("blue"), 40, 40)
player.rect.topleft = (50, 50)

target = Box(pygame.Color("red"), 40, 40)
target.rect.topleft = (random.randint(100, 400), random.randint(100, 300))

# Sprite group
sprites = pygame.sprite.Group(player, target)

# Control variables
running = True
won = False
clock = pygame.time.Clock()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        player.move(dx, dy)

        if player.rect.colliderect(target.rect):
            won = True

    # Drawing
    screen.fill((255, 255, 255))  # White background
    sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color("green"))
        screen.blit(win_text, (
            (SCREEN_WIDTH - win_text.get_width()) // 2,
            (SCREEN_HEIGHT - win_text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
