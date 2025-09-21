import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define custom colors
GOLD = pygame.Color("gold")
AQUA = pygame.Color("aqua")
TEAL = pygame.Color("teal")

SPRITE_COLORS = [GOLD, AQUA, TEAL]
BACKGROUND_COLORS = [GOLD, AQUA, TEAL]

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        # Bounce on left\right
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] *= -1
            boundary_hit = True

        # Bounce on top\bottom
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] *= -1
            boundary_hit = True

        # Post events if boundary hit
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice(SPRITE_COLORS))

# Change background color
def change_background_color():
    global bg_color
    bg_color = random.choice(BACKGROUND_COLORS)

# Set up screen
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")

bg_color = random.choice(BACKGROUND_COLORS)

# Create sprite
sp1 = Sprite(GOLD, 20, 30)
sp1.rect.x = random.randint(0, 470)
sp1.rect.y = random.randint(0, 370)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(sp1)

clock = pygame.time.Clock()
exit_game = False

# Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()
