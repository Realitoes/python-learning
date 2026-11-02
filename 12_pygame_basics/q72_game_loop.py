# Q72: keep the window open until the X is clicked
# Start with your 3 lines from Q71, then add the game loop underneath.
# Before you run it, write down what you think will happen,
# and what will happen when you click the X.

import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()