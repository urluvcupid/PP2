import pygame 
import random

pygame.init()

screen = pygame.display.set_mode((1000, 555))
screen.fill((255, 255, 255))

done = False

pygame.display.set_caption("something")

block_list = [pygame.Rect(650 + 120 * i, 250 + 70 * j,
                          100, 50) for i in range(3) for j in range(4)]
color_list = [(random.randrange(0, 255),
               random.randrange(0, 255), random.randrange(0, 255))
              for i in range(3) for j in range(4)]

for i, block in enumerate(block_list):
    pygame.draw.rect(screen, color_list[i], block)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
