import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 15

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Shapes Version")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

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

        # Key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        # Key up
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_WIDTH))

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move them off-screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        draw_enemy(enemyX[i], enemyY[i])

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

    draw_player(playerX, playerY)
    show_score(10, 10)
    pygame.display.update()
