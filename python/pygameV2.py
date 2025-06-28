import pygame
pygame.init(); screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get(): done = event.type == pygame.QUIT
    screen.fill((0, 0, 0)); pygame.draw.rect(screen, (8, 125, 255), (30, 30, 60, 68)); pygame.display.flip()
