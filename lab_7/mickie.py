import pygame
import os
import datetime
screen = pygame.display.set_mode((830, 780))
image = pygame.image.load('Mainclock.png').convert_alpha()
left = pygame.image.load('leftHand.png').convert_alpha()
right = pygame.image.load('Right hand.png').convert_alpha()
pygame.display.set_caption("Mickey")
def Rotate_Center(surface, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_bord = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surface.blit(rotated_image, new_bord)

def seconds_angle(theta):
    result =((second % 60) / 60) * -(360)
    return result

def minute_angle(theta):
    result = ((minute % 60) / 60) * -(360-40)
    return result

pygame.init()
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    screen.blit(image, (0,0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second

    Rotate_Center(screen, left, (180, 320), seconds_angle(second))
    Rotate_Center(screen, right, (160, 300), minute_angle(minute))

    pygame.display.flip()
    clock.tick(60)