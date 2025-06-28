import math
import random
import pygame

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Shapes Version")

# Clock to control frame rate
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game constants
PLAYER_START_X = 370
PLAYER_START_Y = 380
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
PLAYER_SPEED = 3

ENEMY_WIDTH = 50
ENEMY_HEIGHT = 30
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 30
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
COLLISION_DISTANCE = 27
NUM_ENEMIES = 6

BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED_Y = 6
bullet_state = "ready"

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Player setup
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy setup
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for _ in range(NUM_ENEMIES):
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet setup
bulletX = 0
bulletY = playerY

# Score
score_value = 0

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, RED)
    screen.blit(over_text, (200, 250))

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, PLAYER_WIDTH, PLAYER_HEIGHT))

def draw_enemy(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, ENEMY_WIDTH, ENEMY_HEIGHT))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, RED, (x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, y, BULLET_WIDTH, BULLET_HEIGHT))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0

    # Update player position
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_WIDTH))

    # Enemy movement
    for i in range(NUM_ENEMIES):
        if enemyY[i] > 340:
            for j in range(NUM_ENEMIES):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Check collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        draw_enemy(enemyX[i], enemyY[i])

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= BULLET_SPEED_Y
        if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"

    # Draw everything
    draw_player(playerX, playerY)
    show_score(10, 10)
    pygame.display.update()
    clock.tick(60)  # Cap the frame rate at 60 FPS
