# Q84: score - count how many foods the snake eats
# Your Q83 code is below. Add a score:
#   1) Make a box called score that starts at 0.
#   2) Every time the snake eats, add 1 to it.
#   3) When the game ends, print it in the terminal like:  Score: 3
# Think: where does each of those three lines go? (Remember your hot = [] slip in Q62.)

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
score = 0
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
    
    if x == food_x and y == food_y:
        food_x = 20 * random.randint(0, 29)
        food_y = 20 * random.randint(0, 19)
        score = score + 1
    
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.draw.rect(screen, "red", (food_x, food_y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
print("Score:", score)
pygame.quit()
