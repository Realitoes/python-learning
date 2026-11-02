# Q78: move in steps of one square (grid movement)
# Your Q77 code is below. Make two changes:
#   1. Each step should move a whole square (20 pixels) instead of 1 pixel.
#      Change the numbers you give dx and dy (keep the + and - the same way round).
#      Don't forget the starting dy at the top.
#   2. Slow the loop down from 60 times a second to 10 times a second.
# Before you run it, write down:
#   a) How many pixels per second did the square move in Q77?
#   b) How many pixels per second will it move now?
#   c) Will the movement look smooth or jumpy?

import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
x = 100
y = 50
dx = 0
dy = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 20
                dy = 0
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 20
            elif event.key == pygame.K_LEFT:
                dx = -20
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -20

    x = x + dx
    y = y + dy
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
