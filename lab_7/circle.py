import pygame
WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.display.set_caption("Moving Ball")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2 
radius = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    # Update ball position based on key presses, but ensure it stays within boundaries
    x = max(radius, min(x + (pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]) * 7, WIDTH - radius))
    y = max(radius, min(y + (pressed[pygame.K_DOWN] - pressed[pygame.K_UP]) * 7, HEIGHT - radius))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()