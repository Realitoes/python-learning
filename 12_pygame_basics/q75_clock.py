# Q75: slow it down with a clock
# Start with your working code from Q74.
# Then:
#   1. BEFORE the while loop:   clock = pygame.time.Clock()
#   2. at the END of the while loop (after flip):   clock.tick(60)
# Before you run it, work out: about how many SECONDS will the square
# take to go from x = 100 to the right edge (x = 600)?

import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
x = 100
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = x + 1
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, 50, 20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()