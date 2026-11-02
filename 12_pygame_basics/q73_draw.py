# Q73: draw the snake's head
# Start with your working code from Q72, then add the drawing lines
# inside the while loop (after the for loop).
# Before you run it, write down WHERE in the window you think the square will be.

import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.draw.rect(screen, "green", (100, 50, 20, 20))
    pygame.display.flip()
pygame.quit()