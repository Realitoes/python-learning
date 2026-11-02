# Q77: steer with the arrow keys
# Your Q76 code is below. Inside the "for event" loop, add code that:
#   - checks if the event is a key being pressed down  (pygame.KEYDOWN)
#   - then checks WHICH key it was (event.key), and changes dx and dy:
#       pygame.K_RIGHT -> move right
#       pygame.K_LEFT  -> move left
#       pygame.K_UP    -> move up
#       pygame.K_DOWN  -> move down
# Before you run it, write down: what will the square do when you LET GO of a key?

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 1
                dy = 0
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1
            elif event.key == pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -1
            
    x = x + dx
    y = y + dy
    screen.fill("black")
    pygame.draw.rect(screen, "green", (x, y, 20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

#hi