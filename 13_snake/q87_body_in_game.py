# Q87: put the body in the game (it moves as 3 squares, it doesn't grow yet)
# Your Q84 code is below. Change it so:
#   1) Before the loop, make a box called body holding 3 squares, with the head (x, y) LAST:
#      [[60, 40], [80, 40], [100, 40]]
#   2) Each step, after x and y change: add the new head [x, y] to the end of body,
#      then remove the tail (Q86).
#   3) Instead of drawing one green square at (x, y), use a for loop to draw
#      EVERY square in body. Hint: for square in body: ... then square[0] is its x, square[1] is its y.
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
body = [[60, 40], [80, 40], [100, 40]]
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
    for b in [x, y]:
        pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.draw.rect(screen, "red", (food_x, food_y, 20, 20))
    pygame.display.flip()
    clock.tick(10)
print("Score:", score)
pygame.quit()

body.append([x, y])
body.pop(0)

#i'm so gay