# Q80: put a food square in a random spot on the grid
# Your Q78 code is below. Add code that:
#   1. imports the random toolbox (at the top, next to import pygame)
#   2. BEFORE the loop: makes a box food_x. Pick a random column (0 to 29),
#      then turn the column number into pixels. (Column 3 starts at what x?)
#      Do the same for food_y with a random row (0 to 19).
#   3. Draws a red 20x20 square at food_x, food_y.
#      (Where does drawing go? After the screen is wiped, before it's shown.)
# Before you run it, write down:
#   a) The biggest number food_x could ever be.
#   b) The biggest number food_y could ever be.

import pygame
import random 

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

x = 100
y = 50
dx = 0
dy = 0
food_x = 20 * random.randint(0, 29)
food_y = 20 * random.randint(0, 19)
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
    pygame.draw.rect(screen, "red", (food_x, food_y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
