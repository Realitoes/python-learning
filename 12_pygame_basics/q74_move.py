# Q74: make the square move
# Start with your working code from Q73.
# Then:
#   1. BEFORE the while loop, make a box called x that starts at 100
#   2. in the draw.rect line, use x instead of 100
#   3. inside the while loop, add 1 to x every time round
# Before you run it, write down what you think the square will do.

import pygame
pygame.init()
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
pygame.quit()
