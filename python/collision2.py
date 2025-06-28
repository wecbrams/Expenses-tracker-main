import pygame
import random
import math

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
OBJECT_SIZE = 40
SPEED = 0.1
FONT_SIZE = 64

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Objects Collision")
font = pygame.font.SysFont("Arial", FONT_SIZE)
clock = pygame.time.Clock()

# Sprite class
class MovingObject(pygame.sprite.Sprite):
    def __init__(self, color, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((OBJECT_SIZE, OBJECT_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.target_pos = target_pos
        self.velocity = self.calculate_velocity()

    def calculate_velocity(self):
        dx = self.target_pos[0] - self.rect.centerx
        dy = self.target_pos[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance == 0:
            return [0, 0]
        return [SPEED * dx / distance, SPEED * dy / distance]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

# Create two objects moving toward each other
obj1_start = (50, 200)
obj2_start = (450, 200)

object1 = MovingObject(pygame.Color("blue"), obj1_start, obj2_start)
object2 = MovingObject(pygame.Color("red"), obj2_start, obj1_start)

# Sprite group
all_sprites = pygame.sprite.Group(object1, object2)

# Game state
running = True
won = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        all_sprites.update()
        if object1.rect.colliderect(object2.rect):
            won = True

    screen.fill((255, 255, 255))  # White background
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color("green"))
        screen.blit(win_text, (
            (SCREEN_WIDTH - win_text.get_width()) // 2,
            (SCREEN_HEIGHT - win_text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
