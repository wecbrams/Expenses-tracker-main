import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color Changing Sprite")
    
    colors = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white")
    }
    current_color = colors["white"]
    x, y = 30, 30
    sprite_width, sprite_height = 60, 68
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= 3
        if keys[pygame.K_RIGHT]: x += 3
        if keys[pygame.K_UP]: y -= 3
        if keys[pygame.K_DOWN]: y += 3

        # Boundary collision and color change logic
        if x <= 0:
            current_color = colors["blue"]
        elif x + sprite_width >= screen_width:
            current_color = colors["yellow"]
        elif y <= 0:
            current_color = colors["red"]
        elif y + sprite_height >= screen_height:
            current_color = colors["green"]
        else:
            current_color = colors["white"]

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
