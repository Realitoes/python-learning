# Q90: make the body move. ONE change: two new lines.
# Every step, add the new head [x, y] to the end of body, then remove the tail (like Q86).
# Think carefully about WHERE they go:
#   - after x and y change? before?
#   - inside an if? or every step?
#   - inside the while loop, or after it?
#
# Before running: what will you see when you press the arrow keys?
# My prediction:
#
import pygame
import random

#sets clock
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))

#variables
x = 100
y = 40
dx = 0
dy = 0
food_x = 20 * random.randint(0, 29)
food_y = 20 * random.randint(0, 19)
score = 0
body = [[60, 40], [80, 40], [100, 40]]
running = True

#main loop
while running:
    #movement/quit code
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

    #wall boundries
    if x < 0 or x > 580 or y < 0 or y > 380:
        running = False

    #food randomisation
    if x == food_x and y == food_y:
        food_x = 20 * random.randint(0, 29)
        food_y = 20 * random.randint(0, 19)
        score = score + 1

    #display output
    screen.fill("black")
    for b in body:
        pygame.draw.rect(screen, "green", (b[0], b[1], 20, 20))
    pygame.draw.rect(screen, "red", (food_x, food_y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
print("Score:", score)
pygame.quit()
