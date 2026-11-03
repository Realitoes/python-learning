# Q83: walls - game over if the snake leaves the window
# Your Q82 code is below. After the snake moves, add ONE if that uses "or" to check
# whether the snake has gone off the left, the right, the top OR the bottom.
# If it has, end the game (how did you stop the loop when the window's X was clicked?).
# Before you write it, work out:
#   a) The biggest x the snake can have and still be fully on screen (it's 20 wide, the window is 600).
#   b) If you drive straight right, what x will the snake be at when the game ends?

import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

x = 100
y = 40
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

    if x < 0 or x > 580 or y < 0 or y > 380:
        running = False
    if y < 0 or y > 380:
        running = False
    
    if x == food_x and y == food_y:
        food_x = 20 * random.randint(0, 29)
        food_y = 20 * random.randint(0, 19)
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.draw.rect(screen, "red", (food_x, food_y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
