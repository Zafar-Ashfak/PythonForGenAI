import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First pygame Program")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 30)

# Clock
clock = pygame.time.Clock()

# Player
x = 350
y = 250
size = 50
speed = 5

running = True

while running:

    # FPS
    clock.tick(60)

    # Background
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    # Draw player
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    # Draw circle
    pygame.draw.circle(screen, RED, (150, 100), 50)

    # Draw line
    pygame.draw.line(screen, GREEN, (0, 0), (800, 600), 5)

    # Draw ellipse
    pygame.draw.ellipse(screen, YELLOW, (500, 100, 180, 80))

    # Draw text
    text = font.render("Move the Blue Box with Arrow Keys", True, BLACK)
    screen.blit(text, (120, 20))

    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()