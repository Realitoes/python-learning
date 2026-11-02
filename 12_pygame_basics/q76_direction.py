# Q76: direction boxes
# Your Q75 code is below. Change it so that:
#   1. BEFORE the loop, add a box y that starts at 50
#   2. BEFORE the loop, add two direction boxes:  dx = 0  and  dy = 1
#   3. inside the loop, replace  x = x + 1  with two lines that add dx to x, and dy to y
#   4. in the draw.rect line, use y instead of 50
# Before you run it, write down which way you think the square will move.

import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
x = 100
y = 50
dx = 0
dy = 1
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = x + dx
    y = y + dy
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
